# CSCI4140-Project
A web application for photo style transferring.

# Dependency
```
Tensorflow
Flask
WTForms
```
# How to Run
1. Download 6 model styles (ckpt files) from [here](https://drive.google.com/drive/folders/0B9jhaT37ydSyRk9UX0wwX3BpMzQ) into a new directory(For example: model_styles/). 
2. Set PROJECT_PATH and APP_PATH in deployment/run_server.py
4. Add empty directory: deployment/static/images/
5. in deployment/ directory, using following command line: 
```
FLASK_APP=run_server.py flask run
```
