from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'test'}}

@app.get('/about')
def about():
    return {'data':{'about':'FastAPI is a modern, fast, and lightweight web framework for building APIs with Python.'}}

#Dynamic routing should be below any static routing (jaise yaha par id int fix h to ise niche rakhna h)
#Example:
# Note: Pydantic takes care of all the data validation part under the wood. 
@app.get('/blog/unpublished')
def unpublished():
    return {"data": "Unpublished blog posts"}

@app.get('/blog/{id}')
def show(id:int): #to set the return type of the data
    return {"data":id}

@app.get('/blog/{id}/comments')
def comment(id):  
    return {f"data {id}": {1,2,3,4,5,6,7,8}}


# Getting request body 
class Blog(BaseModel):
    name:str
    price: float
    tax: float | None = None
    published:Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {"data": blog.name}
 
 