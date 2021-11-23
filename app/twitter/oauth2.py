from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from twitter import schemas, database, models
from sqlalchemy.orm.session import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="twitter")

SECRET_KEY = "10a7368e2cd0e83e8008d8f106d34811ef2902cfd9608df7ce03ea440d345fda"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
   
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def verify_token_and_get_current_user(token: str = Depends(oauth2_scheme), db:Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.email == token_data.email).first()

    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: schemas.User = Depends(verify_token_and_get_current_user)):
    if not current_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user