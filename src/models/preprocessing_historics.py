from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Text
from models.base_class import Base
from sqlalchemy.sql import func


class PreprocessingHistorics(Base):
    __tablename__ = 'preprocessing_historics'
    id = Column(Integer, primary_key=True)
    input = Column(Text, nullable=False)
    output = Column(Text, nullable=False)
    step = Column(String(255), nullable=False)
    dataset_id = Column(ForeignKey('datasets.id'), nullable=False)
    processing_time = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())
