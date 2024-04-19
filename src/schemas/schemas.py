from pydantic import BaseModel
from typing import Union


class InputDoc(BaseModel):
    name: str
    size: int
    link: str
    
    class Config:
        orm_mode = True

class PreprocessingInput(BaseModel):
    input:str
    output:str
    step:str
    processing_time:int

class CorpusInput(BaseModel):
    corpus:str

class UsersInput(BaseModel):
    name:str
    senha:str
    email:str

class ReviewInput(BaseModel):
    title: str
    review: str
    rating: int
    recomend_product: bool

class ProcessDataInput(BaseModel):
    review_id : Union[int, None]
    preprocessing_id : Union[int, None]
    data: str

class ProductsInput(BaseModel):
    id_category : Union[int, None]
    name:str
    product_id:str
    brand:str

class CategoryInput(BaseModel):
    category:str

class SubCategoryInput(BaseModel):
    id_category : Union[int, None]
    subcategory:str