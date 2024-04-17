from schemas.schemas import PreprocessingInput
from sqlalchemy.orm import Session
from models.preprocessing_historics import PreprocessingHistorics
from models.datasets import Datasets
from fastapi import HTTPException



class PreprocessingHistoricsController:
    def insert_register(self, dataset_id: int, preprocessing_data: PreprocessingInput, db: Session):
        dataset = db.query(Datasets).filter(Datasets.id == dataset_id).first()
        if dataset is None:
            raise HTTPException(status_code=404, detail="Document not found")
        new_preprocessing = PreprocessingHistorics(
            input=preprocessing_data.input,
            output=preprocessing_data.output,
            step=preprocessing_data.step,
            dataset_id=dataset_id,
            processing_time=preprocessing_data.processing_time
        )
        db.add(new_preprocessing)
        db.commit()
        return {"message": "Preprocessing data inserted successfully"}



    def get_register(self, dataset_id: int, db: Session):
        doc = db.query(Datasets).filter(Datasets.id == dataset_id).first()
        preprocessings = db.query(PreprocessingHistorics).filter(PreprocessingHistorics.dataset_id == dataset_id).all()
        if doc is None:
            raise HTTPException(status_code=404, detail="Preprocessing not found")
        return preprocessings