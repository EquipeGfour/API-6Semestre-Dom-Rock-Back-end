from models.docs import Docs
from schemas.schemas import InputDoc
from sqlalchemy.orm import Session
from fastapi import HTTPException


class Doc:
    def get_doc_id(self, doc_id: int, db: Session):
        doc = db.query(Docs).filter(Docs.id == doc_id).first()
        if doc is None:
            raise HTTPException(status_code=404, detail="Document not found")
        return doc

    def get_doc(self, db: Session):
        doc = db.query(Docs).all()
        if doc is None:
            raise HTTPException(status_code=404, detail="Documents not found")
        return doc