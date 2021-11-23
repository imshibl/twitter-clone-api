from passlib.context import CryptContext
from passlib.utils.decor import deprecated_function

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def hashPassword(plain_password):
        return pwd_context.hash(plain_password)
    
    def verifyPassword(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)