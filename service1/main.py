from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# God model
class God(Base):
    __tablename__ = "gods"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    religion = Column(String(100))
    power = Column(String(200))


# Pydantic model for God
class GodSchema(BaseModel):
    name: str
    religion: str
    power: str

    class Config:
        orm_mode = True


# Endpoint to health check
@app.get("/healthy")
def health_check():
    return {"status": "healthy"}


# Endpoint to retrieve all gods
@app.get("/gods", response_model=List[GodSchema])
def get_gods():
    try:
        db = SessionLocal()
        gods = db.query(God).all()
        db.close()
        return gods
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
