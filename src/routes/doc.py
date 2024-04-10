from secrets import token_hex
from fastapi import APIRouter, Depends
from db.db import get_db
from sqlalchemy.orm import Session
from modules.doc import Doc
from schemas.schemas import InputDoc
from fastapi import File, UploadFile, Depends
from models.docs import Docs
import os

router = APIRouter()


@router.post("/inserir", description="Rota para inserir as informações do arquivo enviados via upload")
async def create_doc(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_ext = file.filename.split(".")[-1]
    file_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    new_doc = Docs(
        document_name=file.filename,
        size=len(content),
        link=file_path
    )
    db.add(new_doc)
    db.commit()
    return {"message": "Documento criado com sucesso"}


@router.get("/get", description="Rota para buscar as informações de um documento por id")
def get_doc_by_id(doc_id: int, db: Session = Depends(get_db)):
    return Doc().get_doc_id(doc_id, db)

@router.get("/all", description="Rota para buscar todas as informações dos documentos salvos")
def get_all_docs(db: Session = Depends(get_db)):
    return Doc().get_doc(db)
