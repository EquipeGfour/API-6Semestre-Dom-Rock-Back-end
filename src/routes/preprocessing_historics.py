from fastapi import APIRouter, Depends
from db.db import get_db
from sqlalchemy.orm import Session
from schemas.schemas import PreprocessingInput
from modules.preprocessing_historics import PreprocessingHistorics


router = APIRouter()

@router.post("/insert", description="Rota inserir um registro de pré-processamento")
def insert_preprocessing_register(doc_id: int, preprocessing_data: PreprocessingInput, db: Session = Depends(get_db)):
    return PreprocessingHistorics().insert_register(doc_id, preprocessing_data, db)

@router.get("/get", description="Rota para buscar o ultimo registro de pré-processamento")
def get_preprocessing_register(doc_id: int, db: Session = Depends(get_db)):
    return PreprocessingHistorics().get_register(doc_id, db)
