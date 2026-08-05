from pydantic import BaseModel

class userData(BaseModel):
    username: str
    password: str

