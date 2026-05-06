from fastapi import Request
from fastapi.templating import Jinja2Templates
from app.presentation.get_height_weight_info import router

templates = Jinja2Templates(directory="frontend/templates")

@router.get("/body_info/{user_id}")
def get_body_info_page(request: Request, user_id: int):
    context = {
        "request": request,
        "user_id": user_id
    }
    return templates.TemplateResponse(
        request=request,
        name="body_info.html",
        context=context
    )