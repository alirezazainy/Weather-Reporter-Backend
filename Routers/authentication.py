from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from DB.database import get_db
from DB import db_user
from schemas import UserBase
from fastapi.security import OAuth2PasswordRequestForm
# Authentication Router

# Generate Router Instance
router = APIRouter(tags=['authentication'])


@router.post("/token")
async def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Gives Generated token from 'getUserToken' Method to UI/UX in a Dictionary
    """
    access_token = db_user.getUserToken(request, db)
    if not access_token:
        raise HTTPException(400, detail='invalid credentials')

    else:
        return {
            'access_token': access_token,
            'type_token': 'bearer'
        }
