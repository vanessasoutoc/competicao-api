from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# from ..pontuacoes.schemas import PontuacaoBase as Pontuacao


class CompeticaoBase(BaseModel):
    titulo: str
    data_fim: Optional[datetime] = None


class CompeticaoRequest(CompeticaoBase):
    ...


class CompeticaoResponse(CompeticaoBase):
    id: int

    class Config:
        from_attributes = True
