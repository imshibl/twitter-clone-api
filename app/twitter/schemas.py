from pydantic import BaseModel
from typing import Optional,List

class User(BaseModel):
    name: str
    email: str
    password: str

class TweetBase(BaseModel):
    tweet:str



class Login(BaseModel):
    email:str
    password:str



class Tweet(TweetBase):
    id:int
    class Config():
        orm_mode=True

class ShowUserName(BaseModel):
    id:int
    name:str
    class Config():
        orm_mode=True



class Following(BaseModel):
    followee_id:int
    followee_name:str

    class Config():
        orm_mode=True


    

class Followers(BaseModel):
    follower_id:int
    follower_name:str


    
    class Config():
        orm_mode=True




class CurrentUserProfile(BaseModel):
    id:int
    name:str
    email:str
    password:str

    tweets:List[Tweet]
    user_following:List[Following]
    user_followers:List[Followers]

    class Config():
        orm_mode = True



class ShowTweet(BaseModel):
    tweet:str
    creator: ShowUserName

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    id:int
    name:str
    email:str

    tweets:List[Tweet]
    user_following:List[Following]
    user_followers:List[Followers]

    class Config():
        orm_mode = True




class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None