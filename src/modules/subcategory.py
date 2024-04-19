from models.subcategory import SubCategory
from schemas.schemas import SubCategoryInput
from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.db import SessionLocal


class SubCategoryController:
    def create_subcategory(self, subcategory_data: SubCategoryInput):
        db = SessionLocal()
        try:
            subcategory = SubCategory(
                id_category=subcategory_data.id_category,
                subcategory=subcategory_data.subcategory
            )
            db.add(subcategory)
            db.commit()
            db.refresh(subcategory)
            return subcategory
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()


    def get_subcategory_data_by_id(self, subcategory_id: int):
        db = SessionLocal()
        subcategory_data = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
        
        if subcategory_data is None:
            raise HTTPException(status_code=404, detail="Subcategory not found")
        
        return subcategory_data


    def get_all_subcategory_datas(self):
        db = SessionLocal()
        datas = db.query(SubCategory).all()
        if datas is None:
            raise HTTPException(status_code=404, detail="Subcategorys not found")
        return datas

