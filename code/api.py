import ray, pickle
from ray import serve

ray.init(address='auto')
client = serve.start(detached=True, http_options={"host": "0.0.0.0"})

class LogRegModel:
    def __init__(self):
        with open('code/data/model.pickle', 'rb') as f:
            self.clf = pickle.load(f)
        
        with open('code/data/tfidf.pickle', 'rb') as f:
            self.vectorizer = pickle.load(f)
            
    async def __call__(self, starlette_request):
        v = await starlette_request.json()
        
        # convert from JSON payload to TFIDF
        features = self.vectorizer.transform([v['post']])
        prediction = self.clf.predict(features)
        
        return { "body": v['post'], "prediction": prediction }
    
client.create_backend('logreg', LogRegModel, config={"num_replicas": 3})
client.create_endpoint('predict', backend="logreg", route="/predict")