from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from models.base_class import Base
from sqlalchemy.sql import func

class SubCategory(Base):
    __tablename__ = 'subcategory'
    id = Column(Integer, primary_key=True)
    id_category = Column(ForeignKey('category.id'), nullable=False)
    subcategory = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())