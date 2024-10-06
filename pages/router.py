
from fastapi import APIRouter, Request, Form, status, HTTPException
from fastapi.templating import Jinja2Templates

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
def postdata(request: Request,ticker=Form(), period = Form(), start_date= Form()):
    main(ticker, period, start_date)
    MCAD = f"/static/{ticker}_{period}_MACD.png"
    RSI = f"/static/{ticker}_{period}_RSI.png"
    Stock = f"/static/{ticker}_{period}_stock_price_chart.png"
    # if main.st is None:
    #     return HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail='Ticker was not found')
    return templates.TemplateResponse("output.html", {"request": request, 'RSI': RSI, 'Stock' :Stock, 'MCAD': MCAD})


