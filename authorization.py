from datetime import datetime, timedelta

from fastapi import Depends, status, HTTPException, Security
from fastapi.security import (
    OAuth2PasswordBearer,
    SecurityScopes,
)
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from DB.database import get_db
from DB import db_user
from schemas import UserBase, TokenData
# Authorization Processor

# Generate OAuth2 Bearer Instance
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", scopes={
                                     '105':'isAdmin',
                                     'User':'User'
                                     })

# Secret Key and other details
SECRET_KEY = "d6ad91a1df806697cca646fdb40a950d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Access token Creator 
    this Func create and manage tokens with timedelta and jwt packages

    Returns am encoded jason web token 
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Check the token and Returns User who has that token
    """
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    error_credential = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                     detail='invalid credentials',
                                     headers={'WWW-authenticate': 'bearer'})

    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')
        if not username:
            raise error_credential
        token_scopes = _dict.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except JWTError:
        raise error_credential
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value}
            )
    user = db_user.getUser(username, db)

    return user


