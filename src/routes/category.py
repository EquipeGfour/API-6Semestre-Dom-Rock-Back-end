from fastapi import APIRouter, Depends
from db.db import get_db
from sqlalchemy.orm import Session
from modules.category import CategoryController
from schemas.schemas import CategoryInput


router = APIRouter()


@router.post("/insert", description="Rota para inserir Categoria")
def create_category(data:CategoryInput, db: Session = Depends(get_db)):
    return CategoryController().create_category(data, db)

@router.get("/get", description="Rota para buscar Categoria por id")
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    return CategoryController().get_category_id(category_id, db)

@router.get("/all", description="Rota para buscar todas as Categorias salvas")
def get_all_category(db: Session = Depends(get_db)):
    return CategoryController().get_category(db)
