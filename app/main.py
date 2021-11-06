from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root_get():
    return {"message": "OK"}

@app.post('/')
def root_post():
    return {"message": "OK"}

@app.get('/healthz')
def health_check():
    return {"health":"OK"}

@app.get('/readyz')
def ready_check():
    return {"ready":"true"}
