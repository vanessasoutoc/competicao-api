from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from v1.competicoes.router import router as v1_competicoes_router

origins = [
    '*'
]

Base.metadata.create_all(bind=engine)

route = APIRouter(prefix='/api')

@route.get('/health')
def healt_check():
    return {
        'health':'ok'
    }

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(title='CompeticoesApi', swagger_ui_parameters={'syntaxHighlight': False})

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

route.include_router(v1_competicoes_router, prefix='/v1')
app.include_router(route)
