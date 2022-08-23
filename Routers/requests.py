from fastapi import APIRouter, Depends, HTTPException, Security, BackgroundTasks
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from DB.database import get_db
from DB.db_weather import getCities, saveCityInfo, getaCity
from schemas import CityDisplay, CityReq
from authorization import get_current_user
from schemas import UserBase, UserDisplay
from authorization import oauth2_scheme
from Sources.SheetGenerator.sheetgenerator import newExcel
# Requests Router

# Generate Router Instance
router = APIRouter(prefix="/request", tags=['Request'])

# Background Task of Get info from irimo.ir


def scheduler(db: Session):
    """
    Background task to update immediately cities information
    """
    info = saveCityInfo(db)
    if info == 400:
        raise HTTPException(400, detail='data can\'t be updated')


@router.get("/weather/all", response_model=list[CityDisplay])
async def getCitiesWeather(task: BackgroundTasks, current_user: UserBase = Security(get_current_user, scopes=["User"]), db: Session = Depends(get_db)):
    """
    Get All Cities Information
    """
    task.add_task(scheduler, db)
    cities = getCities(db)
    if not current_user.isAdmin:
        if current_user.reqlimit > 0:
            current_user.reqlimit -= 1
        else:
            raise HTTPException(403, detail='your requests was on limit')
    return cities


@router.post("/weather/custom", response_model=list[CityDisplay])
async def getCityWeather(request: CityReq, task: BackgroundTasks, current_user: UserBase = Security(get_current_user, scopes=["User"]), db: Session = Depends(get_db)):
    """
    Get Custom cities information 
    , for using this rout you need have city IDs and you can get and save them from 'request/weather/all'
    """
    task.add_task(scheduler, db)
    cities = getaCity(request, db)
    if not current_user.isAdmin:
        if current_user.reqlimit > 0:
            current_user.reqlimit -= 1
        else:
            raise HTTPException(403, detail='your requests was on limit')
    return cities


@router.post("/weather/excel")
async def getWeatherExcel(request: CityReq, task: BackgroundTasks, current_user: UserBase = Security(get_current_user, scopes=["User"]), db: Session = Depends(get_db)):
    """
    Get an excel file from custom cities
    , for using this rout you need have city IDs and you can get and save them from '/request/weather/all'
    """
    task.add_task(scheduler, db)
    cities = getaCity(request, db)
    code = newExcel(current_user.username, cities)
    if not current_user.isAdmin:
        if current_user.reqlimit > 0:
            current_user.reqlimit -= 1
        else:
            raise HTTPException(403, detail='your requests was on limit')
    return FileResponse("C:\\Users\\rayan\\Desktop\\Weather Reporter\\Back-End (FastAPI)\\Files\\"+code, media_type='application/octet-stream', filename=code)
