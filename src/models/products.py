from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean
from models.base_class import Base
from sqlalchemy.sql import func

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300), nullable=False)
    product_id = Column(String(200), nullable=False)
    brand = Column(String(200), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())