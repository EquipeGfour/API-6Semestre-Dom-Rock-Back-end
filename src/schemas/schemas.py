from pydantic import BaseModel


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
