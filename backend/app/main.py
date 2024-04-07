from fastapi import FastAPI
from app.databases import engine
import app.models as models
from app.api import router as api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TODO App")

app.include_router(api_router)