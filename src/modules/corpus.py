from models.corpus import Corpus
from schemas.schemas import CorpusInput
from sqlalchemy.orm import Session
from fastapi import HTTPException


class Corpus:
    def create_corpus(self, data:CorpusInput,db: Session ):
        new_corpus = Corpus(text = data.text)
        db.add(new_corpus)
        db.commit()
        return {"message": "Corpus created successfully"}


    def get_corpus_id(self, corpus_id: int, db: Session):
        lex = db.query(Corpus).filter(Corpus.id == corpus_id).first()
        if lex is None:
            raise HTTPException(status_code=404, detail="Corpus not found")
        return lex


    def get_corpus(self, db: Session):
        lex = db.query(Corpus).all()
        if lex is None:
            raise HTTPException(status_code=404, detail="Corpus not found")
        return lex
