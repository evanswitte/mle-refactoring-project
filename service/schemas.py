from pydantic import BaseModel, Field


class HousePost(BaseModel):
    bedrooms: int = Field(description="Number of bedrooms")
    bathrooms: float = Field(description="Number of bathrooms")
    floors: float = Field(description="How many floors")
    zipcode: int = Field(description="Which side of King County ( Zipcode )")
    price: int = Field(description="Last sold price")
    last_change: int = Field(description="year of the last renovation")

    class Config:
        orm_mode = True


class HouseGet(BaseModel):
    bedrooms: int = Field(description="Number of bedrooms")
    bathrooms: float = Field(description="Number of bathrooms")
    floors: float = Field(description="How many floors")
    zipcode: int = Field(description="Which side of King County ( Zipcode )")
    price: int = Field(description="Last sold price")

    class Config:
        orm_mode = True


class HouseUpdate(BaseModel):
    price: int = Field(description="Last sold price")
    last_change: int = Field(description="year of the last renovation")

    class Config:
        orm_mode = True
