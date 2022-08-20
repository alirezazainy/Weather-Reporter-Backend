from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from DB.database import get_db
from DB import db_weather
from schemas import UserBase
from authorization import get_current_user
# Requests Router

# Generate Router Instance
router = APIRouter(prefix="/request", tags=['Request'])



@router.get("/weather")
async def getCityWeather():
    pass

@router.get("/weather/excel")
async def getWeatherExcel():
    pass