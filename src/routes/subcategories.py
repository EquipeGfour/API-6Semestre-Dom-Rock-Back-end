from fastapi import APIRouter
from modules.subcategories import SubCategoriesController
from schemas.schemas import SubCategoryInput


router = APIRouter()


@router.post("/insert", description="Rota para inserir uma subcategoria")
def create_subcategory(data:SubCategoryInput):
    return SubCategoriesController().create_subcategory(data)

@router.get("/get", description="Rota para buscar uma subcategoria")
def get_subcategory_by_id(subcategory_id: int):
    return SubCategoriesController().get_subcategory_data_by_id(subcategory_id)

@router.get("/all", description="Rota para buscar todas as subcategorias")
def get_all_subcategory():
    return SubCategoriesController().get_all_subcategory_datas()