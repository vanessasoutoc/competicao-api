from pydantic import BaseModel

class PontuacaoBase(BaseModel):
    competicao_id: int
    atleta: str
    valor: float
    unidade: str


class PontuacaoRequest(PontuacaoBase):
    ...


class PontuacaoResponse(PontuacaoBase):
    id: int

    class Config:
        from_attributes = True
