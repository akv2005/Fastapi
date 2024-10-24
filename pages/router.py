import os
import shutil

from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path
from moex import main
from  data_download import LastNlines

router =APIRouter(
    prefix="/pages",
    tags=['Pages']
)

templates = Jinja2Templates(directory="templates")

@router.get("/input")
def get_input_page( request: Request):
    return templates.TemplateResponse("input.html", {"request": request})

@router.post("/postdata")
def postdata(request: Request,ticker=Form(), period = Form(), start_date= Form()):
    main(ticker, period, start_date)
    MCAD = f"/static/{ticker}_{period}_MACD.png"
    RSI = f"/static/{ticker}_{period}_RSI.png"
    STD = f"/static/{ticker}_{period}_std_dev_chart.png"
    SPC = f"/static/{ticker}_{period}_stock_price_chart.png"

    info_ = LastNlines('py.log')    # Выбор двух последних строк py.log
    fff = Path(f"static/{ticker}_{period}_MACD.png") #  Проверка на наличие созданного файла
    if fff.exists() is False:
        content = {"request": request, 'ticker': ticker}
        return templates.TemplateResponse("output_error.html", content)

    int_ = {'1':'1 минута', '10': '10 минут', '60':'1 час', '24':'1 день', '7':'1 неделя', '31': '1 месяц'}
    for key in int_:
        if key == period:
            interval = int_[key]


    content = {"request": request, 'RSI': RSI,
               'MCAD': MCAD, 'info_': info_, 'STD': STD, 'SPC': SPC,
               'period': period, 'interval': interval,
               }

    return templates.TemplateResponse("output.html", content)

@router.get("/delete")
def get_delete_page(request: Request):
    shutil.rmtree('./static/')
    os.mkdir('./static')
    return templates.TemplateResponse("base.html", {"request": request})