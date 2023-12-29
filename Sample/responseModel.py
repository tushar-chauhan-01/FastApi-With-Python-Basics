from pydantic import BaseModel

class successRes(BaseModel):
    code: str
    msg: str
    data: list
    

class failRes(BaseModel):
    code: str
    msg: str
    data: list
    