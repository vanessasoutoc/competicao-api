from sqlalchemy.orm import Session

from .model import Pontuacao


class PontuacaoRepository:
    @staticmethod
    def list_all(db: Session) -> list[Pontuacao]:
        return db.query(Pontuacao).all()

    @staticmethod
    def save(db: Session, pontuacao: Pontuacao) -> Pontuacao:
        if pontuacao.id:
            db.merge(pontuacao)
        else:
            db.add(pontuacao)
        db.commit()
        return pontuacao
