from models.datasets import Datasets
from schemas.schemas import InputDoc
from sqlalchemy.orm import Session
from fastapi import HTTPException


class Datasets:
    def get_dataset_id(self, doc_id: int, db: Session):
        dataset = db.query(Datasets).filter(Datasets.id == doc_id).first()
        if dataset is None:
            raise HTTPException(status_code=404, detail="Dataset not found")
        return dataset

    def get_datasets(self, db: Session):
        dataset = db.query(Datasets).all()
        if dataset is None:
            raise HTTPException(status_code=404, detail="Datasets not found")
        return dataset
