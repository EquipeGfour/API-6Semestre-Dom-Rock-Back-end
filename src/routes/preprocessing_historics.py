from fastapi import APIRouter, Depends
from db.db import get_db
from sqlalchemy.orm import Session
from schemas.schemas import PreprocessingInput
from modules.preprocessing_historics import PreprocessingHistoricsController


router = APIRouter()

@router.post("/insert", description="Rota inserir um registro de pré-processamento")
def insert_preprocessing_register(dataset_id: int, preprocessing_data: PreprocessingInput, db: Session = Depends(get_db)):
    return PreprocessingHistoricsController().insert_register(dataset_id, preprocessing_data, db)

@router.get("/get", description="Rota para buscar o ultimo registro de pré-processamento")
def get_preprocessing_register(dataset_id: int):
    return PreprocessingHistoricsController().get_register(dataset_id)
