from DB.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
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

    
class Admin(Base):
    """
    Admin Table ORM model
    generate Admin table
    """
    __tablename__ = "Admins"

    ID = Column(Integer, index=True, primary_key=True)
    AID = Column(String)
    password = Column(String)
    email = Column(String)
    token = Column(String)
    