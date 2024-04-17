from fastapi import APIRouter, Depends
from db.db import get_db
from sqlalchemy.orm import Session
from modules.corpus import CorpusController
from schemas.schemas import CorpusInput


router = APIRouter()


@router.post("/insert", description="Rota para inserir Corpus")
def create_corpus(data:CorpusInput, db: Session = Depends(get_db)):
    return CorpusController().create_corpus(data, db)

@router.get("/get", description="Rota para buscar os Corpus por id")
def get_corpus_by_id(corpus_id: int, db: Session = Depends(get_db)):
    return CorpusController().get_corpus_id(corpus_id, db)

@router.get("/all", description="Rota para buscar todos os Corpus salvos")
def get_all_corpus(db: Session = Depends(get_db)):
    return CorpusController().get_corpus(db)
