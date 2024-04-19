from fastapi import APIRouter
from modules.process_data import ProcessDataController
from schemas.schemas import ProcessDataInput



router = APIRouter()


@router.post("/insert", description="Rota para inserir uma dado processado")
def create_corpus(data:ProcessDataInput):
    return ProcessDataController().insert_process_data(data)

@router.get("/get", description="Rota para buscar por um dado processado")
def get_corpus_by_id(process_id: int):
    return ProcessDataController().get_process_data_by_id(process_id)

@router.get("/all", description="Rota para buscar todos os dados processados")
def get_all_corpus():
    return ProcessDataController().get_all_process_datas()

