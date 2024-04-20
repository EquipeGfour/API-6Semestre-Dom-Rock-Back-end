from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from modules.processing_errors import ProcessingErrorController
from schemas.schemas import ProcessingErrorInput

router = APIRouter()

@router.post("/insert", description="Route to create a new processing error")
def create_processing_error(error_data: ProcessingErrorInput, db: Session = Depends(get_db)):
    return ProcessingErrorController().create_processing_error(error_data, db)

@router.get("/all", description="Route to fetch all processing errors")
def get_all_processing_errors(db: Session = Depends(get_db)):
    return ProcessingErrorController().get_all_processing_errors(db)

@router.get("/get", description="Route to fetch a processing error by ID")
def get_processing_error_by_id(error_id: int, db: Session = Depends(get_db)):
    error = ProcessingErrorController().get_processing_error_by_id(error_id, db)
    if not error:
        raise HTTPException(status_code=404, detail="Processing error not found")
    return error

