from twitter import schemas, models
from fastapi import HTTPException
from sqlalchemy.orm import Session


def post(request: schemas.Tweet, db:Session, creator_id:int):
    new_tweet = models.Tweet(tweet=request.tweet, creator_id=creator_id)
    db.add(new_tweet)
    db.commit()
    db.refresh(new_tweet)
    return new_tweet

def get_all(db:Session):
    tweets = db.query(models.Tweet).all()
    return tweets

def delete(tweet_id:int, db:Session):
    tweet = db.query(models.Tweet).filter(models.Tweet.id == tweet_id).delete(synchronize_session=False)
    db.commit()
    if not tweet:
        raise HTTPException(status_code=404, detail="item not found")
    return {"detail": "deleted"}
