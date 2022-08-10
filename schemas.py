from pydantic import BaseModel
from datetime import datetime
# Request & Response Schemas


class UserBase(BaseModel):
    """
    Request User Protected Information 
    """
    username: str 
    password: str 
    email: str 


class UserDisplay(BaseModel):
    """
    Response User Public Information
    """
    username: str
    email: str

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    """
    Request User Authentication Information
    """
    username: str
    password: str

    class Config:
        orm_mode = True

