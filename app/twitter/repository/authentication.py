from sqlalchemy.orm import Session

from twitter import schemas, models, oauth2
from fastapi import HTTPException
from twitter.hashing import Hash




def create_user(request: schemas.User, db:Session):
    hashed_password = Hash.hashPassword(request.password)
    username = db.query(models.User).filter(models.User.name == request.name).first()
    email = db.query(models.User).filter(models.User.email == request.email).first()
    if username:
         raise HTTPException(status_code=403, detail="username not available")
    if email:
         raise HTTPException(status_code=403, detail="email is already in use")

    new_user = models.User(name = request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    access_token = oauth2.create_access_token(
        data= {"sub": new_user.email}
    )
    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }

def login_user(request:schemas.Login, db:Session):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
         raise HTTPException(status_code=404, detail="Invalid credentials")
    if not Hash.verifyPassword(request.password, user.password):
        raise HTTPException(status_code=404, detail="Invalid password")

    access_token = oauth2.create_access_token(
        data= {"sub": user.email}
    )
    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
