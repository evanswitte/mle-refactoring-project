from database import Base
from pydantic import BaseModel
from sqlalchemy import Column, Float, Integer
from sqlalchemy.orm import validates


class House(Base):
    __tablename__ = "houses"
    id = Column(Integer, primary_key=True, index=True)
    bedrooms = Column(Integer)
    bathrooms = Column(Float)
    floors = Column(Float)
    zipcode = Column(Integer)
    price = Column(Integer)
    last_change = Column(Integer)

    @validates("zipcode")
    def validate_zipcode(self, key, value):
        if value is None:
            return None
        if not isinstance(value, int):
            raise ValueError("zipcode must be an integer")
        if not (10000 <= value <= 99999):
            raise ValueError("zipcode must have exactly 5 digits")
        return value

    @validates("last_change")
    def validate_last_change(self, key, value):
        if value is None:
            return None
        if not isinstance(value, int):
            raise ValueError("last_change must be an integer")
        if not (1000 <= value <= 9999):
            raise ValueError("last_change must have exactly 4 digits")
        return value
