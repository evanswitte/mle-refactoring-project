import models
import schemas
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session

app = FastAPI(
    title="King County Real Estate API",
    description="Welcome to the King County Houses Real Estate API. This API is a user-friendly API that provides access to historical real estate price data in the King County region. It offers developers and real estate professionals a quick and easy way to access accurate and up-to-date information on house prices.",
    version="0.0.1",
)

models.Base.metadata.create_all(bind=engine)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return {"detail": exc.errors(), "body": exc.body}


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def index() -> Response:
    """Welcome to King County API."""
    return Response(
        "For more information how to use this API, visit http://localhost:8000/docs"
    )


# get all houses from the database
@app.get("/houses", response_model=list[schemas.HouseGet])
def get_all_house(db: Session = Depends(get_db)):
    """List all houses from the database"""
    house = db.query(models.House).all()
    if not house:
        raise HTTPException(status_code=404, detail="House does not exist")
    return house


# add house to database
@app.post("/houses", response_model=schemas.HouseGet)
def create_house(request: schemas.HousePost, db: Session = Depends(get_db)):
    """Adds a new house to the database"""
    new_house = models.House(
        bedrooms=request.bedrooms,
        bathrooms=request.bathrooms,
        floors=request.floors,
        zipcode=request.zipcode,
        price=request.price,
        last_change=request.last_change,
    )
    db.add(new_house)
    db.commit()
    db.refresh(new_house)
    return new_house


# update house
@app.put("/houses/{id}")
def update_house(id: int, request: schemas.HouseUpdate, db: Session = Depends(get_db)):
    """Updates the last year of renovation and the price of the House"""
    house = db.query(models.House).filter(models.House.id == id)
    if not house.first():
        raise HTTPException(status_code=404, detail="House does not exist")
    house.update(request.dict())
    db.commit()
    return "Updated successfully"


# delete house
@app.delete("/houses/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    """Deletes the house from the database"""
    house = db.query(models.House).filter(models.House.id == id)
    if not house.first():
        raise HTTPException(status_code=404, detail="House does not exist")
    house.delete(synchronize_session=False)
    db.commit()
    return "Deleted successfully"
