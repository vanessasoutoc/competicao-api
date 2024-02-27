from sqlalchemy.orm import Session

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
