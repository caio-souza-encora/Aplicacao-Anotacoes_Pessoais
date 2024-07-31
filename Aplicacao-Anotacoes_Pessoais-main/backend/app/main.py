from app.connection import Base, engine
from app.views import user_router
from fastapi import FastAPI, APIRouter

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Anotacoes Pessoais",
    docs_url="/docs/",
    openapi_url="/openapi.json/",
)
router = APIRouter()

app.include_router(prefix='/first', router=router)
app.include_router(user_router)