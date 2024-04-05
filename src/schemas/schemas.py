from pydantic import BaseModel

class InputDoc(BaseModel):
    name:str
    size:int
    link:str


class PreprocessingInput(BaseModel):
    input:str
    output:str
    step:str
    processing_time:int