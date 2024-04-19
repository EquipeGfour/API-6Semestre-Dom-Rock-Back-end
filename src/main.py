from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from utils.config import Config
from db.db import engine
from models.base import Base
from routes import dataset_router, preprocessing_historic_router, corpus_router,users_router


config = Config()

project_name = config._g.get("application", "project_name",fallback='service-nibble')
project_version = config._g.get("application", "PROJECT_VERSION",fallback='0.0.0')

app = FastAPI(title=project_name, version=project_version)
app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in ["http://localhost:8000","https://localhost:8000","http://localhost:3000","http://localhost","https://localhost"]],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def create_tables():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return "is running..."

app.include_router(dataset_router, prefix="/dataset", tags=["dataset"])
app.include_router(preprocessing_historic_router, prefix="/pre-processing", tags=["preprocessing"])
app.include_router(corpus_router, prefix="/corpus", tags=["corpus"])
app.include_router(users_router, prefix="/users", tags=["users"])


if __name__ == "__main__":
    print("------------Banco de dados conectado com sucesso!!!------------")
    port = int(config._g.get("application", "port",fallback=8000))
    run("main:app", host="0.0.0.0", port= port, log_level="debug", reload=True)