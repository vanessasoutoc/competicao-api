from pydantic import BaseModel
from ...competicoes.schemas.competicao import CompeticaoResponse

class PontuacaoCompeticaoResponse(BaseModel):
    id: int
    competicao_id: int
    atleta: str
    valor: float
    unidade: str
    competicao: CompeticaoResponse

    class Config:
        from_attributes = True
