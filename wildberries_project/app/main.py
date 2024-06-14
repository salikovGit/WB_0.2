import sys
import os

# Добавьте путь к проекту в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from .api.v1.endpoints import wildberries
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(wildberries.router, prefix="/api/v1", tags=["wildberries"])
