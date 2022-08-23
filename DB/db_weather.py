from Sources.Parsing.parser import parse
from DB.models import City
from schemas import CityReq
from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
from DB.database import get_db
# City to Database Unit of work


def reqCityInfo(parsedstr: str = parse()):
    """
    Request City Information from parser and Unscramble them in a List
    Returns a List
    """
    loc = parsedstr.find("-")
    if parsedstr[loc+1:loc+2] and not parsedstr[loc-1:loc] == '\n' :
        parsedstr = parsedstr.replace('-', '۰° c')
        if parsedstr.find("-"):
            loc = parsedstr.find("-")
            if parsedstr[loc+1:loc+2] and not parsedstr[loc-1:loc] == '\n' :
                parsedstr = parsedstr.replace('-', '۰° c')
            else:
                parsedstr = parsedstr.replace('-', '0')
    else:
        parsedstr = parsedstr.replace('-', '0')
    cities = parsedstr.split("° c")
    lent = len(cities)
    cities.pop(lent - 1)
    cities.pop(lent - 2)
    i = 0
    citylist = []
    for city in cities:
        cit = city.split("\n")
        if i == 0:
            cit.pop(3)
            citylist.append(cit)
        else:
            cit.pop(0)
            cit.pop(0)
            cit.pop(0)
            cit.pop(0)
            cit.pop(3)
            citylist.append(cit)
        i += 1
    return citylist


def saveCityInfo(db: Session, citylist=reqCityInfo()):
    """
    Save Cities Information in DataBase
    Returns a status code
    """
    try:
        for city in citylist:
            dbcit = db.query(City).filter(City.persianname == city[0]).first()
            dbcit.humidity = city[1]
            dbcit.windspeed = city[2]
            dbcit.temperature = city[3]
            db.commit()
            db.refresh(dbcit)
        return 202
    except:
        return 400


def getCities(db: Session):
    """
    Get All of cities information
    """
    city = db.query(City).all()
    return city


def getaCity(request: CityReq, db: Session):
    """
    Get custom Cities information
    """
    ids = request.ID
    citylist = []
    for aid in ids:
        city = db.query(City).filter(City.ID == aid).first()
        citylist.append(city)
    return citylist
