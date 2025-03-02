from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from view.views import view_router
from api.books import book_router
import os

app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")
app.include_router(view_router, prefix="/view")
app.include_router(book_router, prefix="/api")

templates = Jinja2Templates(
    directory=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
)


@app.get(
    "/",
    response_class=HTMLResponse,
    summary="Главна страница",
    description="Просмотр главной страницы в браузере",
)
async def index_page(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Home"}
    )


@app.get(
    "/about/",
    response_class=HTMLResponse,
    summary="Просмотр about",
    description="Просмотр страницы О себе в браузере",
)
async def about_page(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request, "title": "About"}
    )
