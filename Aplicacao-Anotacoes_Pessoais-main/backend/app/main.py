from app.connection import Base, SessionLocal, engine

# from . import models, schemas, crud
from app.schemas import UserLogin
from app.verification import authenticate_user
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Anotacoes Pessoais",
    docs_url="/docs/",
    openapi_url="/openapi.json/",
)


@app.post("/login")
def login(user: UserLogin, db: Session = Depends(SessionLocal)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"message": "Login successful"}
