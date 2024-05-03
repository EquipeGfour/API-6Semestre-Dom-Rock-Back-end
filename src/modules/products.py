from models.products import Products
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from db.db import get_db, SessionLocal
from schemas.schemas import ProductsInput
from models.categories import Categories
from models.subcategories import SubCategories


class ProductsController:
    def create_product(self, product_data: ProductsInput, db: Session = Depends(get_db)):
        new_product = Products(
            name=product_data.name,
            product_id=product_data.product_id,
            id_category=product_data.id_category,
            brand=product_data.brand
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return {"message": "Product data inserted successfully"}

    def get_all_products(self, db: Session):
        return db.query(Products).all()

    def get_product_by_id(self, product_id: int, db: Session):
        product = db.query(Products).filter(Products.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product


    def get_all_products_by_category(self, id_category: int):
        try:
            db = SessionLocal()
            products = db.query(Products).join(
                Categories, Products.id_category == Categories.id).filter(
                    Categories.id == id_category).all()
            return products
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()


    def get_all_products_by_subcategories(self, id_subcategory: int):
        try:
            db = SessionLocal()
            products = db.query(Products).join(
                Categories, Products.id_category == Categories.id).join(
                    SubCategories, SubCategories.id_category == Categories.id).filter(
                        SubCategories.id == id_subcategory).all()
            return products
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()
