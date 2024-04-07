from schemas.schemas import PreprocessingInput
from sqlalchemy.orm import Session
from models.preprocessing import Preprocessing
from models.docs import Docs
from fastapi import HTTPException



class PreProcessing:
    def insert_register(self, doc_id: int, preprocessing_data: PreprocessingInput, db: Session):
        doc = db.query(Docs).filter(Docs.id == doc_id).first()
        if doc is None:
            raise HTTPException(status_code=404, detail="Document not found")
        new_preprocessing = Preprocessing(
            input=preprocessing_data.input,
            output=preprocessing_data.output,
            step=preprocessing_data.step,
            doc_id=doc_id,
            processing_time=preprocessing_data.processing_time
        )
        db.add(new_preprocessing)
        db.commit()
        return {"message": "Preprocessing data inserted successfully"}



    def get_register(self, doc_id: int, db: Session):
        doc = db.query(Docs).filter(Docs.id == doc_id).first()
        preprocessings = db.query(Preprocessing).filter(Preprocessing.doc_id == doc_id).all()
        if doc is None:
            raise HTTPException(status_code=404, detail="Document not found")
        return preprocessings