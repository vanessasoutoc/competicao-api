from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from .model import Pontuacao
from .repository import PontuacaoRepository
from .schemas.pontuacao import PontuacaoResponse, PontuacaoRequest
from .schemas.pontuacao_competicao import PontuacaoCompeticaoResponse

router = APIRouter(prefix='/pontuacoes')

@router.post(
    path='',
    description='Nova pontuação',
    response_model=PontuacaoResponse,
    status_code=status.HTTP_201_CREATED
)
def save(request: PontuacaoRequest, db: Session = Depends(get_db)):
    try:
        pontuacao = PontuacaoRepository.save(db, Pontuacao(**request.dict()))
        return PontuacaoResponse.from_orm(pontuacao)
    except Exception as error:
        raise HTTPException(status_code=404, detail=str('Error %s' % (error)))

@router.get(
    path='',
    description='Lista de competições',
    response_model=list[PontuacaoCompeticaoResponse]
    )
def find_all(db: Session = Depends(get_db)):
    pontuacoes = PontuacaoRepository.list_all(db)
    return [PontuacaoCompeticaoResponse.from_orm(pontuacao) for pontuacao in pontuacoes]
