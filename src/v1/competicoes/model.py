from database import Base
from sqlalchemy import Column, Integer, String, DateTime


class Competicao(Base):
    __tablename__ = "competicoes"

    id: int = Column(Integer, primary_key=True, index=True)
    titulo: str = Column(String(100), nullable=False)
    data_fim: str = Column(DateTime, nullable=True)
