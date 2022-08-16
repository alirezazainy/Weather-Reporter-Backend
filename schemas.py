from pydantic import BaseModel
from typing import List, Union
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
    Response Users Information
    """
    ID: int
    username: str
    email: str
    reqlimit: int
    isAdmin: bool

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


class TokenData(BaseModel):
    username: Union[str, None] = None
    scopes: List[str] = []
