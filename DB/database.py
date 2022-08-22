from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Database Generator

# Create Database SQLAlchemy Engine
engine = create_engine(
    "postgresql://postgres:Alireza16@localhost/WeatherReporter")
# Create Base Class of Database
Base = declarative_base()
# Create Database Session
sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


async def get_db():
    """
    Database Session Instance Generator
    Returns an Instance of Database Session
    """
    session = sessionlocal()
    try:
        yield session
    finally:
        session.close()
