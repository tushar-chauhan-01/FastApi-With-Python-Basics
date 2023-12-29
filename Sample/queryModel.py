from pydantic import BaseModel
class GetQuery(BaseModel):
    query: str