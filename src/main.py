from fastapi import FastAPI
from uvicorn import run
from utils.config import Config
from db.db import engine
from models.base import Base

config = Config()

project_name = config._g.get("application", "project_name",fallback='service-nibble')
project_version = config._g.get("application", "PROJECT_VERSION",fallback='0.0.0')

app = FastAPI(title=project_name, version=project_version)

def create_tables():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return "is running..."

if __name__ == "__main__":
    port = int(config._g.get("application", "port",fallback=8000))
    run("main:app", host="0.0.0.0", port= port, log_level="debug", reload=True)