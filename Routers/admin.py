from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from DB.database import get_db
from DB import db_user
from schemas import UserBase
from authorization import oauth2_scheme
from authorization import isAdmin
# Admin Router

# Generate Router Instance
router = APIRouter(prefix="/105", tags=['admin'])


@router.post("/create")
async def setAdmin(request: UserBase, db: Session = Depends(get_db)):
    """
    Create an Admin and Handle errors during creation

    Returns a status code
    """
    create_user_result = db_user.createAdmin(request, db)
    if create_user_result == 406:
        raise HTTPException(
            406, detail='username or email has registered once')

    elif create_user_result == 201:
        raise HTTPException(201, detail='user created')

    else:
        raise HTTPException(400, detail='creating process has problems')


@router.get('/users')
async def getAllUsers(current_user:UserBase = Depends(isAdmin), db: Session = Depends(get_db)):
    """
    get All Users to admin 
    """
    return db_user.getAllUsers(db)


@router.patch("/limits")
async def changeLimits(current_user:UserBase = Depends(isAdmin), db: Session = Depends(get_db)):
    """
    This function helps Admin to Change Users Request limits 

    Returns a status code
    """
    pass
