from fastapi import FastAPI

from backend.app.presentation import (
    get_user
)
from fastapi.middleware.cors import CORSMiddleware

from backend.app.presentation import (
    create_user,
    get_height_weight_info,
    create_body_info,
    create_foods_info,
    get_intakes_info,
)
from backend.app.presentation.auth import login

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in [
    get_user.router,
    create_user.router,
    get_height_weight_info.router,
    create_body_info.router,
    create_foods_info.router,
    get_intakes_info.router,
    login.router,
]:
    app.include_router(router)

