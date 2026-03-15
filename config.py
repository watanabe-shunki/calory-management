from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.presentation import (
    get_user, create_user, get_height_weight_info, create_body_info
)
from app.infrastructure.session import engine
from app.infrastructure.db.orm_entity.orm_entity import Base
import app.infrastructure.db.orm_entity


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 起動時処理
    Base.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

for router in [
    get_user.router,
    create_user.router,
    get_height_weight_info.router,
    create_body_info.router
]:
    app.include_router(router)


