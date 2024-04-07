from fastapi import APIRouter, Depends
from db.db import get_db
from sqlalchemy.orm import Session
from schemas.schemas import PreprocessingInput
from modules.preprocessing import PreProcessing


router = APIRouter()

@router.post("/insert")
def insert_preprocessing_register(doc_id: int, preprocessing_data: PreprocessingInput, db: Session = Depends(get_db)):
    return PreProcessing().insert_register(doc_id, preprocessing_data, db)

@router.get("/get")
def get_preprocessing_register(doc_id: int, db: Session = Depends(get_db)):
    return PreProcessing().get_register(doc_id, db)
