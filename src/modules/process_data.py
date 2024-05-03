from models.process_data import ProcessData
from db.db import SessionLocal
from fastapi import HTTPException
from schemas.schemas import ProcessDataInput


class ProcessDataController:
    def get_all_process_datas(self):
        try:
            db = SessionLocal()
            datas = db.query(ProcessData).all()
            if datas is None:
                raise HTTPException(status_code=404, detail="Process datas not found")
            return datas
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()

    def get_process_data_by_id(self, process_id: int):
        try:
            db = SessionLocal()
            process_data = db.query(ProcessData).filter(ProcessData.id == process_id).first()
            if process_data is None:
                raise HTTPException(status_code=404, detail="Process data not found")
            return process_data
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()

    def insert_process_data(self, process_data: ProcessDataInput):
        try:
            db = SessionLocal()
            data = ProcessData(
                review_id=process_data.review_id,
                preprocessing_id=process_data.preprocessing_id,
                data=process_data.data
            )
            db.add(data)
            db.commit()
            db.refresh(data)
            return data
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()