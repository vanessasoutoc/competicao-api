from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime


class Competicao(Base):
    __tablename__ = "competicoes"

    id: int = Column(Integer, primary_key=True, index=True)
    titulo: str = Column(String(100), nullable=True)
    data_fim: datetime = Column(DateTime, nullable=True)

    pontuacoes = relationship('Pontuacao', order_by='Pontuacao.valor' , viewonly=True)
