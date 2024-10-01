from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from pages.router import router as router_pages

app = FastAPI(
    title="Trading App"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_pages)

