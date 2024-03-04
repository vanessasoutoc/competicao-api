from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Pontuacao(Base):
    __tablename__ = 'pontuacoes'

    id: int = Column(Integer, primary_key=True, index=True)
    competicao_id: int = Column(Integer, ForeignKey('competicoes.id'))
    atleta: str = Column(String(100), nullable=False)
    valor: float = Column(Float(2,3), nullable=False)
    unidade: str = Column(String(1), nullable=False)

    competicao = relationship('Competicao')
