from fastapi import FastAPI, Depends
from DB.models import Base
from DB.database import engine
from Routers import user, authentication, admin
from authorization import get_current_user
from schemas import UserDisplay, UserBase
# The Main Program

app = FastAPI()
Base.metadata.create_all(engine)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(admin.router)

@app.get('/', response_model= UserDisplay)
async def hello(current_user: UserBase = Depends(get_current_user)):
    return current_user
