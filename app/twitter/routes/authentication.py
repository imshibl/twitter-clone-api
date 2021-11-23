from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from twitter import database, schemas
from typing import List
from twitter.repository import authentication

router = APIRouter(
    tags=["Authentication"],
    prefix="/twitter"
)

get_db = database.get_db


@router.post("/signup")
def signup(request: schemas.User, db:Session = Depends(get_db)):
    return authentication.create_user(request, db)

@router.post("/login")
def login(request:schemas.Login, db:Session = Depends(get_db)):
    return authentication.login_user(request, db)