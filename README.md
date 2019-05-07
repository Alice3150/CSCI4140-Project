# CSCI4140-Project
A web application for photo style transferring.

# Dependency
```
Tensorflow
Flask
WTForms
```
# How to Run
1. Download 6 model styles (ckpt files) from [here](https://drive.google.com/drive/folders/0B9jhaT37ydSyRk9UX0wwX3BpMzQ) into a new directory CSCI4140-Project/model_styles/. 
2. Set PROJECT_PATH and APP_PATH in deployment/run_server.py (BECAREFUL with your path setting!)
4. Add an empty directory: deployment/static/images/
5. In deployment/ directory, using following command line: 
```
FLASK_APP=run_server.py flask run
```
6. Open 127.0.0.1:5000/ in browser
