from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgres://gxrhqrpwbglkcf:3f9e5b26475c94a3ea729e1d06c31b0a9267dbc4f562cba76812d2c612bcb8bc@ec2-54-84-142-90.compute-1.amazonaws.com:5432/dpip3c35l9rhc" 


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


