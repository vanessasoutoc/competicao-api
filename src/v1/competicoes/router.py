from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from .schemas import CompeticaoResponse, CompeticaoRequest
from .repository import CompeticaoRepository
from .model import Competicao

router = APIRouter(prefix='/competicoes')

@router.post("/", response_model=CompeticaoResponse, status_code=status.HTTP_201_CREATED)
def create(request: CompeticaoRequest, db: Session = Depends(get_db)):
    competicao = CompeticaoRepository.save(db, Competicao(**request.dict()))
    return CompeticaoResponse.from_orm(competicao)


@router.get(
    path='',
    description='Lista de competições',
    response_model=list[CompeticaoResponse]
    )
def find_all(db: Session = Depends(get_db)):
    competicoes = CompeticaoRepository.find_all(db)
    return [CompeticaoResponse.from_orm(competicao) for competicao in competicoes]
