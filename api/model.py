from pydantic import BaseModel


class Currency(BaseModel):
    id: int
    code: str
    name: str
    exchange: float

