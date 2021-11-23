from twitter.repository import user
from typing import List
from twitter import database, schemas, oauth2, models
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Users"],
    prefix="/twitter"
)

get_db = database.get_db

@router.get("/users", response_model=List[schemas.ShowUserName])
def get_all_users(db:Session = Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_active_user)):
    return user.get_all(db, current_user)

@router.get("/users/user/me", response_model=schemas.CurrentUserProfile)
def get_my_profile(current_user:schemas.User = Depends(oauth2.get_current_active_user)):
    return current_user


@router.get("/users/user/{username}",response_model=schemas.ShowUser)
def get_selected_user(username: str ,db:Session = Depends(get_db),  current_user:schemas.User = Depends(oauth2.get_current_active_user)):
    return user.get_selected(username, db)

@router.post("/users/user/follow/{user_id}")
def followuser(user_id:int, db:Session = Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_active_user) ):
    
    user = db.query(models.User).filter(models.User.id == user_id).first()
    new_following = models.Following(followee_id=user.id, followee_name=user.name, follower_id=current_user.id)
    new_follower = models.Followers(follower_id=current_user.id, follower_name=current_user.name, followee_id=user.id)
    
    already_followed = db.query(models.Following).filter(models.Following.followee_name == new_following.followee_name).first()

    if already_followed:
        return "already following"
    if user_id == current_user.id:
        return "you can't follow/unfollow you bitch"

    db.add(new_following)
    db.add(new_follower)
    db.commit()
    db.refresh(new_following)
    db.refresh(new_follower)
    return {
        "followed"
    }

@router.delete("/users/user/unfollow/{user_id}")
def unfollowuser(user_id:int, db:Session = Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_active_user)):
    
    following = db.query(models.Following).filter(models.Following.following == user_id, models.Following.follower == current_user.id).delete(synchronize_session=False)
    follower = db.query(models.Followers).filter(models.Followers.follower == current_user.id, models.Followers.following == user_id).delete(synchronize_session=False)
    db.commit()
    if not following or not follower:
        return {
            "you are not following this user"
        }
    if user_id == current_user.id:
        return "you can't follow/unfollow you bitch"
    
    return{
        "unfollowed"
    }





    




