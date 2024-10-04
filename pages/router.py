from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import data_download as dd
import data_plotting as dplt


router =APIRouter(
    prefix="/pages",
    tags=['Pages']
)

templates = Jinja2Templates(directory="templates")

@router.get("/input")
def get_input_page( request: Request):
    stock_data = dd.fetch_stock_data(ticker, period, start_date)
    return templates.TemplateResponse("input.html", {"request": request})

@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/search")
def get_search_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})