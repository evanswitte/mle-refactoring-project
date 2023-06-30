import models
import schemas
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def index() -> Response:
    return Response(
        "Welcome to King County! Have a great time on looking for some interesting Houses"
    )


# get all houses from the database
@app.get("/houses", response_model=list[schemas.HouseGet])
def get_all_house(db: Session = Depends(get_db)):
    house = db.query(models.House).all()
    if not house:
        raise HTTPException(status_code=404, detail="House does not exist")
    return house


# add house to database
@app.post("/houses", response_model=schemas.HouseGet)
def create_house(request: schemas.HousePost, db: Session = Depends(get_db)):
    new_house = models.House(
        bedrooms=request.bedrooms,
        bathrooms=request.bathrooms,
        floors=request.floors,
        zipcode=request.zipcode,
        last_change=request.last_change,
    )
    db.add(new_house)
    db.commit()
    db.refresh(new_house)
    return new_house


# update house
@app.put("/houses/{id}")
def update_user(id: int, request: schemas.HouseUpdate, db: Session = Depends(get_db)):
    house = db.query(models.House).filter(models.House.id == id)
    if not house.first():
        raise HTTPException(status_code=404, detail="House does not exist")
    house.update(request.dict())
    db.commit()
    return "Updated successfully"


# delete house
@app.delete("/houses/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    house = db.query(models.House).filter(models.House.id == id)
    if not house.first():
        raise HTTPException(status_code=404, detail="House does not exist")
    house.delete(synchronize_session=False)
    db.commit()
    return "Deleted successfully"
