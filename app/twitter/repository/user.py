from twitter import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_all(db:Session, current_user:schemas):
    users = db.query(models.User).filter(models.User.id != current_user.id).all()
    return users

def get_selected(username: str, db:Session):
    user = db.query(models.User).filter(models.User.name == username).first()
    if not user:
         raise HTTPException(status_code=404, detail="user not found")
    return user



