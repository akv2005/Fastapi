from lib2to3.fixes.fix_input import context

from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from matplotlib.pyplot import connect

import data_download as dd
import data_plotting as dplt
from moex import main

router =APIRouter(
    prefix="/pages",
    tags=['Pages']
)

templates = Jinja2Templates(directory="templates")

@router.get("/input")
def get_input_page( request: Request):
    return templates.TemplateResponse("input.html", {"request": request})

@router.post("/postdata")
def postdata(request: Request,ticker=Form(), period = Form(), threshold = Form()):
    main(ticker, period, threshold)
    MCAD = f"/static/{ticker}_{period}_MACD.png"
    RSI = f"/static/{ticker}_{period}_RSI.png"
    Stock = f"/static/{ticker}_{period}_stock_price_chart.png"
    return templates.TemplateResponse("output.html", {"request": request, 'RSI': RSI, 'Stock' :Stock, 'MCAD': MCAD})


