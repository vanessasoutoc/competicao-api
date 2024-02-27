from pydantic import BaseModel

from ..competicoes.schemas import CompeticaoResponse

class PontuacaoBase(BaseModel):
    competicao_id: int
    atleta: str
    valor: float
    unidade: str


class PontuacaoRequest(PontuacaoBase):
    ...


class PontuacaoResponse(PontuacaoBase):
    id: int
    competicao: CompeticaoResponse

    class Config:
        from_attributes = True
