from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from twitter import oauth2, schemas, database, models
from twitter.repository import tweet
from typing import List


router = APIRouter(
    prefix="/twitter",
    tags=["Tweets"]    
)

get_db = database.get_db


@router.get("/home", response_model=List[schemas.ShowTweet])
def get_all_tweets(db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_active_user)):
    return tweet.get_all(db)

@router.post("/home/newtweet")
def post_tweet(request: schemas.TweetBase, db:Session = Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_active_user)):
    return tweet.post(request, db, current_user.id)

@router.delete("/myprofile/delete/{tweet_id}")
def delete_tweet(tweet_id:int, db:Session=Depends(get_db),  current_user: schemas.User = Depends(oauth2.get_current_active_user)):
    return tweet.delete(tweet_id, db)


