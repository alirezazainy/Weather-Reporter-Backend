from fastapi import FastAPI, Depends, Security
from DB.models import Base
from sqlalchemy.orm import Session
from DB.database import engine, get_db
from Routers import user, authentication, admin, requests
# The Main Program

app = FastAPI(title="Weather Reporter",
              description="an API to help the Farmers get reports of weather for better farming")
Base.metadata.create_all(engine)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(admin.router)
app.include_router(requests.router)


@app.get('/')
async def hello():
    return "Wellcome to Weather Reporter API"
