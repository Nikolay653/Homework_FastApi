from fastapi import APIRouter
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
import os


view_router = APIRouter(tags=["views"])
templates = Jinja2Templates(directory="templates")

with open(os.path.join(os.getcwd(), "data/data.json"), "r", encoding="utf-8") as file:
    content = json.load(file)
    contents = content["data"]


@view_router.get(
    "/views",
    response_class=HTMLResponse,
    summary="Просмотр списка книг",
    description="Просмотр списка книг в браузере",
)
async def about_page(request: Request):
    return templates.TemplateResponse(
        "views.html",
        {
            "request": request,
            "title": "views",
            "contents": contents,
        },
    )
