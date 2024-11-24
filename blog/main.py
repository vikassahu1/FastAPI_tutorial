from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog,users,authentication
# Initialize FastAPI app
app = FastAPI()

# Create database tables
# models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
#similarly drop_all can be used to drop all tables

app.include_router(blog.router)
app.include_router(users.router)
app.include_router(authentication.router)

# # Endpoint to create a blog
# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
# def create_blog(req: schemas.Blog, db: Session = Depends(get_db)):
#     # Create a new blog object
#     new_blog = models.Blog(title=req.title, body=req.body,user_id = 1)
#     db.add(new_blog)  # Add the blog to the session
#     db.commit()       # Commit the transaction to save it in the database
#     db.refresh(new_blog)  # Refresh the instance to include database defaults like ID
#     return new_blog  # Return the created blog


# #Show a new blog
# @app.get('/blog',response_model = List[schemas.Named],tags=['blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs  = db.query(models.Blog).all()
#     return blogs


#show blog with id 
# @app.get('/blog/{id}',tags=['blogs'])
# def read(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     return blog


# # To delete a blog
# @app.delete('/blog/{id}',status_code = status.HTTP_204_NO_CONTENT,tags=['blogs'])
# def delete(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
#     db.delete(blog)
#     db.commit()


# # To update a blog 
# @app.put('/blog/{id}',status_code = status.HTTP_202_ACCEPTED,tags=['blogs'])
# def update(id:int,req: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
#     blog.title = req.title
#     blog.body = req.body
#     db.commit()
#     db.refresh(blog)
#     return blog


# # <<<<<<<<<<<<<<<<<<<<<<<<    Making user part    >>>>>>>>>>>>>>>>>>>>>>>>>>
# @app.post('/user',tags=['users'])
# def create_user(req: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(name = req.name, email = req.email, password = Hash.bcrypt(req.password))
#     db.add(new_user)  # Add the blog to the session
#     db.commit()       # Commit the transaction to save it in the database
#     db.refresh(new_user)  # Refresh the instance to include database defaults like ID
#     return new_user  # Return the created blog


# @app.get('/user',response_model = List[schemas.ShowUser],tags=['users'])
# def all(db: Session = Depends(get_db)):
#     blogs  = db.query(models.User).all()
#     return blogs
