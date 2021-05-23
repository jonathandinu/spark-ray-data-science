# Scaling Data Science in Python with Spark and Ray


## Getting Started

To run locally in a docker container 👇

```
make jupyter
```

or 

```
docker run -p 8888:8888 -p 8265:8265 -p 8000:8000 -p 8089:8089 -v $(pwd):/home/jovyan/ --pull 'always' psychothan/scaling-data-science
```

Then open a web browser to the URL it spits out (the Jupyter server in the container uses [token authentication](https://jupyter-notebook.readthedocs.io/en/stable/security.html))

![notebook url](images/console.png)
![jupyter notebook](images/notebook.png)


## LICENSE

<p xmlns:cc="http://creativecommons.org/ns#" >This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://jonathanjonathanjonathan.com">Jonathan Dinu</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a></p>

### You are free to:

* __Share__ — copy and redistribute the material in any medium or format
* __Adapt__ — remix, transform, and build upon the material
for any purpose, even commercially.

_The licensor cannot revoke these freedoms as long as you follow the license terms._

### Under the following terms:

* __Attribution__ — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* __No additional restrictions__ — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

### Notices:

You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.

No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.