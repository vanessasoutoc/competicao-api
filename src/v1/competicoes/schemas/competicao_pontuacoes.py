from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from ...pontuacoes.schemas.pontuacao import PontuacaoResponse

class CompeticaoPontuacoesResponse(BaseModel):
    id: int
    titulo: str
    data_fim: Optional[datetime] = None

    pontuacoes: list[PontuacaoResponse]
    class Config:
        from_attributes = True
