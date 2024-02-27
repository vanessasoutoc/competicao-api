from database import get_db
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .model import Pontuacao
from .repository import PontuacaoRepository
from .schemas import PontuacaoResponse, PontuacaoRequest

router = APIRouter(prefix='/pontuacoes')

@router.post(
    path='',
    description='Nova pontuação',
    response_model=PontuacaoResponse,
    status_code=status.HTTP_201_CREATED
)
def create(request: PontuacaoRequest, db: Session = Depends(get_db)):
    pontuacao = PontuacaoRepository.save(db, Pontuacao(**request.dict()))
    return PontuacaoResponse.from_orm(pontuacao)

@router.get(
    path='',
    description='Lista de competições',
    response_model=list[PontuacaoResponse]
    )
def find_all(db: Session = Depends(get_db)):
    pontuacoes = PontuacaoRepository.list_all(db)
    return [PontuacaoResponse.from_orm(pontuacao) for pontuacao in pontuacoes]
