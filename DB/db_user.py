from DB.models import User, Admin
from schemas import UserBase, UserAuth, UserDisplay
from sqlalchemy.orm import Session
from DB.hash import Hash
from authorization import create_access_token
from fastapi import HTTPException
# User to Database Unit of work


def createUser(request: UserBase, db: Session):
    """
    Create a User and save it to the Database 
    this Func check the Email and UserName if Registered couldn't Register again with same information
    and save the User in the Database Users Table

    Returns a status code if created 201 and else 406
    """
    # Handling Exceptions
    try:
        # Check Email and Username
        if not db.query(User).filter(User.username == request.username or User.email == request.email).first():
            # Register new User
            user = User(
                username=request.username,
                password=Hash.bcrypt(request.password),
                email=request.email,
                token=None,
                reqlimit=3
            )

            db.add(user)
            db.commit()
            db.refresh(user)

            result = 201
            return result
        # If Username or Email Registered once User can't Register again with them
        else:
            result = 406
            return result
    except:
        raise HTTPException(400, detail='something went wrong')


def getUserToken(request: UserAuth, db: Session):
    """
    Generates, save and returns User token with create_access_token Method
    """
    user = db.query(User).filter(User.username == request.username).first()
    # Check User is Registered or not
    if not user:
        raise HTTPException(401, detail='invalid credentials')
    elif Hash.verify(user.password, request.password):
        access_token = create_access_token(data={'sub': user.username})
        user.token = access_token
        db.commit()
        db.refresh(user)
        return user.token
    else:
        raise HTTPException(401, detail='invalid credentials')


def getUser(username: str, db: Session):
    """
    Returns User Information From Database with Check primary username
    """
    user = db.query(User).filter(User.username == username).first()
    if not user:
        user = db.query(Admin).filter(Admin.AID == username).first()
        return user
    return user


def updateUser(request: UserBase, token: str, db: Session):
    """
    Updating User credentials
    checking Database Table information for set primary email and username

    Returns a status code
    """
    user = db.query(User).filter(User.token == token).first()
    # Checking username and email are itself or not
    if db.query(User).filter(User.username == request.username or User.email == request.email).first():
        if user.username == request.username and user.email == request.email:
            user.password = Hash.bcrypt(request.password)
            db.commit()
            db.refresh(user)
            result = 202
            return result
        elif user.username == request.username and not user.email == request.email:
            result = 4061  # 4061 means email exist
            return result
        elif not user.username == request.username and user.email == request.email:
            result = 4062  # 4062 means username exist
            return result
        else:
            result = 406
            return result
    else:
        user.username = request.username
        user.email = request.email
        user.password = Hash.bcrypt(request.password)
        db.commit()
        db.refresh(user)
        result = 202
        return result


def getAllUsers(db: Session):
    return db.query(User).all()


def createAdmin(request: UserBase, db: Session):
    """
    Create a Admin and save it to the Database 
    this Func check the Email and UserName if Registered couldn't Register again with same information
    and save the User in the Database Admin Table

    Returns a status code if created 201 and else 406
    """
    # Handling Exceptions
    try:
        # Check Email and Username
        if not db.query(Admin).filter(Admin.AID == request.username or Admin.email == request.email).first():
            # Register new User
            admin = Admin(
                AID="@"+request.username,
                password=Hash.bcrypt(request.password),
                email=request.email,
                token=None
            )

            db.add(admin)
            db.commit()
            db.refresh(admin)

            result = 201
            return result
        # If Username or Email Registered once User can't Register again with them
        else:
            result = 406
            return result
    except:
        raise HTTPException(400, detail='something went wrong')


def getAdminToken(request: UserAuth, db: Session):
    """
    Create a Admin and save it to the Database 
    this Func check the Email and UserName if Registered couldn't Register again with same information
    and save the Admin in the Database Admins Table

    Returns a status code if created 201 and else 406
    """
    admin = db.query(Admin).filter(Admin.AID == "@"+request.username).first()
    if not admin:
        raise HTTPException(401, detail='invalid credentials')
    elif Hash.verify(admin.password, request.password):
        access_token = create_access_token(data={'sub': admin.AID})
        admin.token = access_token
        db.commit()
        db.refresh(admin)
        return admin.token
    else:
        raise HTTPException(401, detail='invalid credentials')
