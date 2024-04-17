from secrets import token_hex
from fastapi import APIRouter, Depends, Response
from db.db import get_db
from sqlalchemy.orm import Session
from modules.datasets import Datasets
from schemas.schemas import InputDoc
from fastapi import File, UploadFile, Depends
from models.datasets import Datasets
import os

router = APIRouter()
# C:\API - DomRock - BackEnd\BackEnd\API-6Semestre-Dom-Rock-Back-end
# Caminho absoluto para o diretório 'uploads'
path = os.path.abspath(os.getcwd()) 
upload_path = os.path.join(path, 'uploads')

@router.post("/inserir", description="Rota para inserir as informações do arquivo enviados via upload", status_code=200)
async def create_doc(file: UploadFile = File(...), db: Session = Depends(get_db), response:Response = 200):
    file_ext = file.filename.split(".")[-1]
    file_path = os.path.join(upload_path, file.filename)
    os.makedirs("uploads", exist_ok=True)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    new_doc = Datasets(
        name=file.filename,
        size=len(content),
        link=file_path
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)  # Atualiza o objeto new_doc com as informações do banco de dados
    return new_doc

@router.get("/get", description="Rota para buscar as informações de um documento por id")
def get_doc_by_id(doc_id: int, db: Session = Depends(get_db)):
    return Datasets().get_doc_id(doc_id, db)

@router.get("/all", description="Rota para buscar todas as informações dos documentos salvos")
def get_all_docs(db: Session = Depends(get_db)):
    return Datasets().get_doc(db)
