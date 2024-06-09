from sqlalchemy.orm import Session
from models import MyHealthData
from database import engine, Base, get_session

Base.metadata.create_all(bind=engine)