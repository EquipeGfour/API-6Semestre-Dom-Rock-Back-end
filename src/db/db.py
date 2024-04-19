from utils.config import Config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.datasets import Base
from models.preprocessing_historics import Base
from models.corpus import Base
from models.users import Base

config = Config()

SQLALCHEMY_DATABASE_URI = config._g.get("application", "uri")

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

def get_db() -> SessionLocal: # type: ignore
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
