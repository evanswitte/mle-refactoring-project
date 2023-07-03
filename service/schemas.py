from typing import Optional

from pydantic import BaseModel, Field, confloat, conint


class HousePost(BaseModel):
    bedrooms: conint(gt=0) = Field(
        description="It represents the count of separate rooms intended for sleeping"
    )
    bathrooms: confloat(gt=0.0) = Field(
        description="It represents the count of separate areas containing toilet and bathing facilities"
    )
    floors: confloat(ge=0.0) = Field(
        description="It represents the count of levels or stories in the building structure"
    )
    zipcode: conint(ge=10000, le=99999) = Field(
        description="The 5-digit ZIP code representing the location in King County"
    )
    price: conint(ge=1) = Field(
        description="Last sold price. It represents the price at which the house was last sold"
    )
    last_change: Optional[conint(ge=1000, le=9999)] = Field(
        description="Year of the last renovation of the house. It indicates the most recent year when renovations or improvements were made.",
    )

    class Config:
        orm_mode = True


class HouseGet(BaseModel):
    bedrooms: int = Field(
        description="It represents the count of separate rooms intended for sleeping"
    )
    bathrooms: float = Field(
        description="It represents the count of separate areas containing toilet and bathing facilities"
    )
    floors: float = Field(
        description="It represents the count of levels or stories in the building structure"
    )
    zipcode: int = Field(
        description="The 5-digit ZIP code representing the location in King County"
    )
    price: int = Field(
        description="Last sold price. It represents the price at which the house was last sold"
    )
    last_change: Optional[conint(ge=1000, le=9999)] = Field(
        description="Year of the last renovation of the house. It indicates the most recent year when renovations or improvements were made.",
    )

    class Config:
        orm_mode = True


class HouseUpdate(BaseModel):
    price: conint(ge=1) = Field(
        description="Last sold price. It represents the price at which the house was last sold"
    )
    last_change: Optional[conint(ge=1000, le=9999)] = Field(
        None,
        description="Year of the last renovation of the house. It indicates the most recent year when renovations or improvements were made.",
    )

    class Config:
        orm_mode = True
