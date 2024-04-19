from fastapi import APIRouter
from modules.subcategory import SubCategoryController
from schemas.schemas import SubCategoryInput


router = APIRouter()


@router.post("/insert", description="Rota para inserir uma subcategoria")
def create_subcategory(data:SubCategoryInput):
    return SubCategoryController().create_subcategory(data)

@router.get("/get", description="Rota para buscar uma subcategoria")
def get_subcategory_by_id(subcategory_id: int):
    return SubCategoryController().get_subcategory_data_by_id(subcategory_id)

@router.get("/all", description="Rota para buscar todas as subcategorias")
def get_all_subcategory():
    return SubCategoryController().get_all_subcategory_datas()