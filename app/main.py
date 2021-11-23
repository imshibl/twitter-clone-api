from twitter.routes import authentication, user, tweet
from fastapi import FastAPI

from twitter import models
from twitter.database import engine



app = FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(tweet.router)