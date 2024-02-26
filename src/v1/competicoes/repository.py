from sqlalchemy.orm import Session

from .model import Competicao

class CompeticaoRepository:
    @staticmethod
    def find_all(db: Session) -> list[Competicao]:
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
    def find_by_id(db: Session, id: int) -> Competicao:
        return db.query(Competicao).filter(Competicao.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Competicao).filter(Competicao.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        competicao = db.query(Competicao).filter(Competicao.id == id).first()
        if competicao is not None:
            db.delete(competicao)
            db.commit()
