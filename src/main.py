from http.client import HTTPException
from fastapi import Depends, FastAPI
from uvicorn import run
from models.docs import Docs
from models.preprocessing import Preprocessing
from utils.config import Config
from db.db import engine
from models.base import Base
from db.db import SessionLocal
from sqlalchemy.orm import Session
from schemas.schemas import InputDoc, PreprocessingInput

config = Config()

project_name = config._g.get("application", "project_name",fallback='service-nibble')
project_version = config._g.get("application", "PROJECT_VERSION",fallback='0.0.0')

app = FastAPI(title=project_name, version=project_version)

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()  
    try:
        yield db
    finally:
        db.close()

@app.post("/docs")
def create_doc(data:InputDoc,db: Session = Depends(get_db)):
    new_doc = Docs(document_name = data.name,size = data.size,link = data.link)
    db.add(new_doc)
    db.commit()
    return {"message": "Document created successfully"}

@app.get("/docs/{doc_id}")
def get_doc_id(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Docs).filter(Docs.id == doc_id).first()
    if doc is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc


@app.post("/docs/preprocessing/{doc_id}")
def create_preprocessing(doc_id: int, preprocessing_data: PreprocessingInput, db: Session = Depends(get_db)):
    doc = db.query(Docs).filter(Docs.id == doc_id).first()
    if doc is None:
        raise HTTPException(status_code=404, detail="Document not found")
    new_preprocessing = Preprocessing(
        input=preprocessing_data.input,
        output=preprocessing_data.output,
        step=preprocessing_data.step,
        doc_id=doc_id,
        processing_time=preprocessing_data.processing_time
    )
    db.add(new_preprocessing)
    db.commit()
    return {"message": "Preprocessing data inserted successfully"}

@app.get("/")
def read_root():
    return "is running..."

if __name__ == "__main__":
    port = int(config._g.get("application", "port",fallback=8000))
    run("main:app", host="0.0.0.0", port= port, log_level="debug", reload=True)