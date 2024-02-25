from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware


origins = [
    '*'
]

route = APIRouter(prefix='/api')

@route.get('/health')
def healt_check():
    return {
        'health':'ok'
    }

app = FastAPI(title='CompetitionApi', swagger_ui_parameters={'syntaxHighlight': False})

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# route.include_router(v1_creditcard_router, prefix='/v1')
app.include_router(route)
