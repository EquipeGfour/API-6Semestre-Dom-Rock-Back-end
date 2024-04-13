from fastapi import FastAPI
from uvicorn import run
from utils.config import Config
from db.db import engine
from models.base import Base
from routes import doc_router, preprocessing_router, lexico_router


config = Config()

project_name = config._g.get("application", "project_name",fallback='service-nibble')
project_version = config._g.get("application", "PROJECT_VERSION",fallback='0.0.0')

app = FastAPI(title=project_name, version=project_version)

def create_tables():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return "is running..."

app.include_router(doc_router, prefix="/document", tags=["document"])
app.include_router(preprocessing_router, prefix="/pre-processing", tags=["preprocessing"])
app.include_router(lexico_router, prefix="/lexico", tags=["lexico"])


if __name__ == "__main__":
    print("------------Banco de dados conectado com sucesso!!!------------")
    port = int(config._g.get("application", "port",fallback=8000))
    run("main:app", host="0.0.0.0", port= port, log_level="debug", reload=True)