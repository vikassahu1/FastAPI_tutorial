from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'test'}}

@app.get('/about')
def about():
    return {'data':{'about':'FastAPI is a modern, fast, and lightweight web framework for building APIs with Python.'}}