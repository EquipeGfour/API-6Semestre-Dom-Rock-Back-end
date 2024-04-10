from fastapi import APIRouter, Depends
from db.db import get_db
from sqlalchemy.orm import Session
from modules.lexicos import Lex
from schemas.schemas import LexicoInput


router = APIRouter()


@router.post("/insert", description="Rota para inserir Lexicos")
def create_lex(data:LexicoInput, db: Session = Depends(get_db)):
    return Lex().create_lex(data, db)

@router.get("/get", description="Rota para buscar os Lexicos por id")
def get_lex_by_id(lex_id: int, db: Session = Depends(get_db)):
    return Lex().get_lex_id(lex_id, db)

@router.get("/all", description="Rota para buscar todos os Lexicos salvos")
def get_all_lexs(db: Session = Depends(get_db)):
    return Lex().get_lex(db)
