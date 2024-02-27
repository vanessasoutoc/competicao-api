from sqlalchemy.orm import Session
from v1.competicoes.model import Competicao

from .model import Pontuacao


class PontuacaoRepository:
    @staticmethod
    def list_all(db: Session) -> list[Pontuacao]:
        return db.query(Pontuacao).all()

    @staticmethod
    def save(db: Session, pontuacao: Pontuacao) -> Pontuacao:
        competicao = db.query(Competicao).filter(Competicao.id == pontuacao.competicao_id).first()

        if competicao:
            if competicao.data_fim:
                raise Exception('Não é possível adicionar pontuação, competição finalizada.')

            if pontuacao.id:
                db.merge(pontuacao)
            else:
                db.add(pontuacao)
            db.commit()
            return pontuacao
        else:
            raise Exception('Competição não encontrada, tente novamente.')

