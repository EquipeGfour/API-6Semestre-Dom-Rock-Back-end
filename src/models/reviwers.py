from sqlalchemy import Column, Integer, String, Enum, Date
from models.base_class import Base

class Reviwer(Base):
    __tablename__ = 'reviwers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    reviewer_id = Column(String(75), nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(Enum('M', 'F'), nullable=False)
    state = Column(String(45), nullable=False)
    created_at = Column(Date, nullable=False)
