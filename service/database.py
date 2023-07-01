import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Retrieve the database connection URL from an environment variable
SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN")

# Create a database engine using the SQLAlchemy create_engine function
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session maker using the SQLAlchemy sessionmaker function
# This session maker will be used to create new sessions to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models using the SQLAlchemy declarative_base function
# This base class will be used as the superclass for all the models in the application
Base = declarative_base()
