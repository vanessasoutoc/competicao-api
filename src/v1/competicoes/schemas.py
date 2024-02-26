from pydantic import BaseModel

class CompeticaoBase(BaseModel):
    titulo: str
    data_fim: str


class CompeticaoRequest(CompeticaoBase):
    ...


class CompeticaoResponse(CompeticaoBase):
    id: int

    class Config:
        orm_mode = True
