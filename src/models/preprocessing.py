from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from models.base_class import Base
from sqlalchemy.sql import func

class Preprocessing(Base):
    __tablename__ = 'preprocessing'
    id = Column(Integer, primary_key=True)
    input = Column(String(255), nullable=False)
    output = Column(String(255), nullable=False)
    step = Column(String(255), nullable=False)
    doc_id = Column(ForeignKey('docs.id'), nullable=False)
    processing_time = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())
    
