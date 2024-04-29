from schemas.schemas import PreprocessingInput
from sqlalchemy.orm import Session
from models.preprocessing_historics import PreprocessingHistorics
from models.datasets import Datasets
from fastapi import HTTPException
from db.db import SessionLocal
from json import loads



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



    def get_register(self, dataset_id: int):
        try:
            db = SessionLocal()
            doc = db.query(Datasets).filter(Datasets.id == dataset_id).first()
            if doc is None:
                raise HTTPException(status_code=404, detail="Preprocessing not found")
            preprocessings = db.query(PreprocessingHistorics).filter(PreprocessingHistorics.dataset_id == dataset_id).all()
            process_objs = list()
            for preprocessing in preprocessings:

                json = loads(preprocessing.output)
                exec_time = 0 
                exec_time += json["noise_remove"]["exec_time"]
                exec_time += json["tokens"]["exec_time"]
                exec_time += json["tokens_without_stop_words"]["exec_time"]
                exec_time += json["expand_abbreviations"]["exec_time"]
                exec_time += json["spell_check"]["exec_time"]

                process_obj = {
                    "id": preprocessing.id,
                    "input": preprocessing.input,
                    "output": json,
                    "step": "",
                    "processing_time": exec_time,
                    "review_type": json["review_type"]
                }

                process_objs.append(process_obj)
            return process_objs
        except Exception as e:
            print(e)
            msg = f"[ERROR] - PreprocessingHistoricsController >> Failed to retrieve preprocesses from dataset {dataset_id}, {str(e)}"
            raise HTTPException(status_code=500, detail=msg)
        finally:
            db.close()