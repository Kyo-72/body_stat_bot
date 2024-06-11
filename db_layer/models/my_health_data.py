# models.py

from sqlalchemy import Column, Integer, Numeric, DateTime
from db_layer.database import Base

class MyHealthData(Base):
    __tablename__ = 'my_health_data'
    __table_args__ = {'extend_existing': True} 
    id     = Column(Integer, primary_key=True, index=True)
    weight = Column(Numeric, nullable=False)
    bfp    = Column(Numeric, nullable=False)
    measurement_datetime = Column(DateTime, nullable=False)
