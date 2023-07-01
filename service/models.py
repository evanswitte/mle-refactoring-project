from database import Base
from pydantic import BaseModel
from sqlalchemy import Column, Float, Integer


class House(Base):
    __tablename__ = "houses"
    id = Column(Integer, primary_key=True, index=True)
    bedrooms = Column(Integer)
    bathrooms = Column(Float)
    floors = Column(Float)
    zipcode = Column(Integer)
    price = Column(Integer)
    last_change = Column(Integer)
