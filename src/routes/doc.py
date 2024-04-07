from fastapi import APIRouter, Depends
from db.db import get_db
from sqlalchemy.orm import Session
from modules.doc import Doc
from schemas.schemas import InputDoc


router = APIRouter()


@router.post("/insert", description="Rota para inserir as informações do arquivo enviados via upload")
def create_doc(data:InputDoc, db: Session = Depends(get_db)):
    return Doc().create_doc(data, db)

@router.get("/get", description="Rota para buscar as informações de um documento por id")
def get_doc_by_id(doc_id: int, db: Session = Depends(get_db)):
    return Doc().get_doc_id(doc_id, db)

@router.get("/all", description="Rota para buscar todas as informações dos documentos salvos")
def get_all_docs(db: Session = Depends(get_db)):
    return Doc().get_doc(db)
