from app.connection import Base, engine
from app.views import user_router, note_router
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Anotacoes Pessoais",
    docs_url="/docs/",
    openapi_url="/openapi.json/",
)


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

app.include_router(prefix='/first', router=router)
app.include_router(user_router)
app.include_router(note_router)