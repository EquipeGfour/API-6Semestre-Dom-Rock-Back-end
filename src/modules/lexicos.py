from models.lexicos import Lexicos
from schemas.schemas import LexicoInput
from sqlalchemy.orm import Session
from fastapi import HTTPException


class Lex:
    def create_lex(self, data:LexicoInput,db: Session ):
        new_lex = Lexicos(text = data.text)
        db.add(new_lex)
        db.commit()
        return {"message": "Document created successfully"}


    def get_lex_id(self, lex_id: int, db: Session):
        lex = db.query(Lexicos).filter(Lexicos.id == lex_id).first()
        if lex is None:
            raise HTTPException(status_code=404, detail="Lexico not found")
        return lex


    def get_lex(self, db: Session):
        lex = db.query(Lexicos).all()
        if lex is None:
            raise HTTPException(status_code=404, detail="Lexicos not found")
        return lex