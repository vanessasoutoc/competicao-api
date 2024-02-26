from sqlalchemy import Column, Integer, String, DateTime

from database import Base

class Competicao(Base):
    __tablename__ = "competicoes"

    id: int = Column(Integer, primary_key=True, index=True)
    titulo: str = Column(String(100), nullable=False)
    data_fim: str = Column(DateTime, nullable=True)
