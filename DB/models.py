from DB.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
# Database Tables ORM Models

class User(Base):
    """
    Users Table ORM model
    generate Users table
    """
    __tablename__ = "Users"

    ID = Column(Integer, index=True, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    token = Column(String)
    reqlimit = Column(Integer)
    isAdmin = Column(Boolean)

class City(Base):
    """
    Cities Table ORM model
    generate Cities table
    """
    __tablename__ = "Cities"

    ID = Column(Integer, index=True, primary_key=True)
    cityname = Column(String)
    persianname = Column(String)
    humidity = Column(Integer)
    temperature = Column(Integer)
    windspeed = Column(Integer)


    