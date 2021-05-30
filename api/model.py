from pydantic import BaseModel


class Currency(BaseModel):
    id: int
    code: str
    exchange: float
