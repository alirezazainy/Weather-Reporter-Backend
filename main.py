from fastapi import FastAPI, Depends, Security
from DB.models import Base
from DB.database import engine
from Routers import user, authentication, admin
from authorization import get_current_user
from schemas import UserBase, UserDisplay
import schedule
import time
from Sources.Parsing.parser import parse
# The Main Program

app = FastAPI(title="Weather Reporter",
              description="an API to help the Farmers give reports of weather for better farming")
Base.metadata.create_all(engine)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(admin.router)
schedule.every().day.at("13:30").do(parse)


@app.get('/', response_model=UserDisplay)
async def hello(current_user: UserBase = Security(get_current_user, scopes=["User"])):
    return current_user
