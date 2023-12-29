from pydantic import BaseModel, validator
from typing import Optional

class Hello(BaseModel):
    firstName: Optional[str]=None
    lastName: Optional[str]=None
    age: Optional[int]=None

    
class HelloBack(BaseModel):
    firstName: str
    lastName: Optional[str]=None
    age: int
