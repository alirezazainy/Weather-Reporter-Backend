from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from DB.database import get_db
from DB import db_user
from schemas import UserBase
from authorization import oauth2_scheme
from authorization import get_current_user
# User Router

# Generate Router Instance
router = APIRouter(prefix="/user", tags=['user'])


@router.post("/create")
async def createUser(request: UserBase, db: Session = Depends(get_db)):
    """
    Create User and Handle Errors During Creating Users

    Returns a status code
    """
    create_user_result = db_user.createUser(request, db)
    if create_user_result == 406:
        raise HTTPException(
            406, detail='username or email has registered once')

    elif create_user_result == 201:
        return HTTPException(201, detail='user created')

    else:
        raise HTTPException(400, detail='creating process has problems')


@router.put('/edit')
async def updateUser(request: UserBase, current_user: UserBase = Depends(get_current_user), db: Session = Depends(get_db)):
    update_user_result = db_user.updateUser(request, current_user.token, db)
    if update_user_result == 202:
        return HTTPException(202, detail='user updated')
    elif update_user_result == 406:
        raise HTTPException(406, detail='username and email are exist')
    elif update_user_result == 4061:
        raise HTTPException(406, detail='email is exist')
    elif update_user_result == 4062:
        raise HTTPException(406, detail='username is exist')
