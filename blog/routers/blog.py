from fastapi import APIRouter, Depends, status, HTTPException # type: ignore
from .. import schemas,models,database,oauth2
from sqlalchemy.orm import Session # type: ignore
from typing import List

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

# Note: Better to make all funtion required in the file in separate folder. 
# Function of router is just to route 


#show blog with id 
@router.get('/{id}')
def read(id: int, db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog



# Endpoint to create a blog
@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(req: schemas.Blog, db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Create a new blog object
    new_blog = models.Blog(title=req.title, body=req.body,user_id = 1)
    db.add(new_blog)  # Add the blog to the session
    db.commit()       # Commit the transaction to save it in the database
    db.refresh(new_blog)  # Refresh the instance to include database defaults like ID
    return new_blog  # Return the created blog



#Show a new blog
@router.get('/',response_model = List[schemas.Named])
def all(db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs  = db.query(models.Blog).all()
    return blogs



# To delete a blog
@router.delete('/{id}',status_code = status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    db.delete(blog)
    db.commit()



# To update a blog 
@router.put('/{id}',status_code = status.HTTP_202_ACCEPTED,tags=['blogs'])
def update(id:int,req: schemas.Blog, db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.title = req.title
    blog.body = req.body
    db.commit()
    db.refresh(blog)
    return blog
