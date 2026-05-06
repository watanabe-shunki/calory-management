from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.presentation.view import get_body_info
from app.presentation import (
    get_user,
    create_user,
    get_height_weight_info,
    create_body_info,
    create_foods_info,
)
from app.infrastructure.session import engine
from app.infrastructure.db.orm_entity.orm_entity import Base
import app.infrastructure.db.orm_entity
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount(path="/static", app=StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="templates")

for router in [
    get_user.router,
    create_user.router,
    get_height_weight_info.router,
    create_body_info.router,
    create_foods_info.router,
    get_body_info.router
]:
    app.include_router(router)


