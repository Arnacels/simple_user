from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from api.api_v1 import api_router
from common.settings import settings
from common import exceptions
from utils.templates import templates

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static",
          StaticFiles(directory=settings.STATIC_DIR, html=True),
          name="static")

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/", response_class=HTMLResponse)
def index_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.exception_handler(exceptions.RepositoryException)
def repository_exception(request: Request,
                         exc: exceptions.RepositoryException):
    return JSONResponse(status_code=400, content=exc.args)
