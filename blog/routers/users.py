from fastapi import APIRouter, Depends, status, HTTPException # type: ignore
from .. import schemas,models,database,oauth2
from sqlalchemy.orm import Session # type: ignore
from ..hashing import Hash 
from typing import List

router = APIRouter(
    prefix='/user',
    tags=['users']
)

# <<<<<<<<<<<<<<<<<<<<<<<<    Making user part    >>>>>>>>>>>>>>>>>>>>>>>>>>
@router.post('/')
def create_user(req: schemas.User, db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_user = models.User(name = req.name, email = req.email, password = Hash.bcrypt(req.password))
    db.add(new_user)  # Add the blog to the session
    db.commit()       # Commit the transaction to save it in the database
    db.refresh(new_user)  # Refresh the instance to include database defaults like ID
    return new_user  # Return the created blog


@router.get('/',response_model = List[schemas.ShowUser])
def all(db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs  = db.query(models.User).all()
    return blogs
