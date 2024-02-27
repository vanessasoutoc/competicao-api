from datetime import datetime
from sqlalchemy.orm import Session
from v1.pontuacoes.model import Pontuacao

from .model import Competicao

class CompeticaoRepository:
    @staticmethod
    def list_all(db: Session) -> list[Competicao]:
        return db.query(Competicao).all()

    @staticmethod
    def save(db: Session, competicao: Competicao) -> Competicao:
        if competicao.id:
            db.merge(competicao)
        else:
            db.add(competicao)
        db.commit()
        return competicao

    @staticmethod
    def finaliza(db: Session, id: int) -> Competicao:
        competicao = db.query(Competicao).filter(Competicao.id == id).first()
        competicao.data_fim = datetime.now()
        db.merge(competicao)
        db.commit()
        return competicao

    @staticmethod
    def ranking(db: Session, id: int) -> Competicao:
        competicao = db.query(Competicao).filter(Competicao.id == id).first()
        return competicao
