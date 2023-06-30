from pydantic import BaseModel


class HousePost(BaseModel):
    bedrooms = int
    bathrooms = float
    floors = float
    zipcode = int
    last_change = int

    class Config:
        orm_mode = True


class HouseGet(BaseModel):
    bedrooms = int
    bathrooms = float
    floors = float
    zipcode = int

    class Config:
        orm_mode = True


class HouseUpdate(BaseModel):
    last_change = int

    class Config:
        orm_mode = True
