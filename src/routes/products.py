from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from modules.products import ProductsController
from schemas.schemas import ProductsInput

router = APIRouter()

@router.post("/insert", description="Route to create a new product")
def create_product(product_data: ProductsInput, db: Session = Depends(get_db)):
    return ProductsController().create_product(product_data, db)

@router.get("/all", description="Route to fetch all products")
def get_all_products(db: Session = Depends(get_db)):
    return ProductsController().get_all_products(db)

@router.get("/get", description="Route to fetch a product by ID")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    return ProductsController().get_product_by_id(product_id, db)