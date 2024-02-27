from database import get_db
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .model import Competicao
from .repository import CompeticaoRepository
from .schemas import CompeticaoResponse, CompeticaoRequest

router = APIRouter(prefix='/competicoes')

@router.post(
    path='',
    description='Nova competições',
    response_model=CompeticaoResponse,
    status_code=status.HTTP_201_CREATED)
def create(request: CompeticaoRequest, db: Session = Depends(get_db)):
    competicao = CompeticaoRepository.save(db, Competicao(**request.dict()))
    return CompeticaoResponse.from_orm(competicao)

@router.get(
    path='',
    description='Lista de competições',
    response_model=list[CompeticaoResponse]
    )
def list_all(db: Session = Depends(get_db)):
    competicoes = CompeticaoRepository.list_all(db)
    return [CompeticaoResponse.from_orm(competicao) for competicao in competicoes]

@router.patch(
    path="/{id}/finaliza",
    description='Finaliza a competição',
    response_model=CompeticaoResponse,
    status_code=status.HTTP_200_OK)
def finaliza(id, db: Session = Depends(get_db)):
    competicao = CompeticaoRepository.finaliza(db, id)
    return CompeticaoResponse.from_orm(competicao)
