from typing import Annotated
from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager
from database import engine
from almoxarifado.routes import router as rotas
import models
@asynccontextmanager
async def lifespan(app: FastAPI):
  models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SAEP")

app.include_router(rotas)


@app.get("/")
def root():
  return {"message": "API rodando com sucesso!"}
