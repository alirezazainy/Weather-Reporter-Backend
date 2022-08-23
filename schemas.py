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
    isAdmin: bool
    reqlimit: int


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
    """
    Response User Token and Auth Data 
    """
    username: Union[str, None] = None
    scopes: List[str] = []


class CityBase(BaseModel):
    """
    Request City Data
    """
    persianname: str
    humidity: str
    temperature: str
    windspeed: str


class CityDisplay(BaseModel):
    """
    Response City Data
    """
    ID: int
    persianname: str
    humidity: str
    temperature: str
    windspeed: str

    class Config:
        orm_mode = True


class CityReq(BaseModel):
    """
    Requests an ID to Display City
    """
    ID: List[int] = ...

    class Config:
        orm_mode = True
