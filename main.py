from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import data_download as dd
import moex
from moex import main

import requests
import data_plotting as dplt

import pages.router
from pages.router import router as router_pages
templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="Trading App"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
#m = moex.main()

@app.get('/')
def get_html(request: Request):
     return templates.TemplateResponse("base.html", {"request": request})


app.include_router(router_pages)

