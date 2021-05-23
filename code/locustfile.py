import time, pickle
import numpy as np
from locust import task, between
from locust.contrib.fasthttp import FastHttpUser

URL = "/predict"

rng = np.random.default_rng(12345)
with open('data/test_data.pickle', 'rb') as f:
    DATA = pickle.load(f)

class ModelUser(FastHttpUser):
    wait_time = between(0.1, 0.2)

    @task
    def get_prediction(self):
        self.client.get(URL, json=self.params)

    def on_start(self):
        index = rng.integers(DATA['X'].shape[0])
        self.params = { 'post' : DATA['X'][index], 'index': int(index)}