from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime



from .database import Base

now = datetime.now()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
   
    account_created_on = Column(DateTime, default=now.strftime('%Y/%m/%d %I:%M:%S'))

    tweets = relationship("Tweet", back_populates="creator")

    user_followers = relationship("Followers", back_populates="user_profile_followers")
    user_following = relationship("Following", back_populates="user_profile_following")

class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    tweet = Column(String)
    creator_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="tweets")


class Followers(Base):
    __tablename__ = "followers"
    id = Column(Integer, primary_key=True, index=True)
    follower = Column(Integer)
    follower_name = Column(String)
    following_id = Column(Integer, ForeignKey("users.id"))
    
    user_profile_followers = relationship("User", back_populates="user_followers")

class Following(Base):
    __tablename__ = "following"
    id = Column(Integer, primary_key=True, index=True)
    following = Column(Integer)
    following_name = Column(String)
    follower_id = Column(Integer, ForeignKey("users.id"))
    
    user_profile_following = relationship("User", back_populates="user_following")
