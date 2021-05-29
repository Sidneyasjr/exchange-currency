from pydantic import BaseModel


class Current(BaseModel):
    id: int
    code: str
    exchange: float
