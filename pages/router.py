from fastapi import APIRouter, Request, Form, status, HTTPException
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
    Stock = f"/static/{ticker}_{period}_stock_price_chart.png"
    info_ = LastNlines('py.log')
    fff = Path(f"static/{ticker}_{period}_MACD.png")

    if fff.exists() is False:
        content = {"request": request, 'ticker': ticker}
        return templates.TemplateResponse("output_error.html", content)

    content = {"request": request, 'RSI': RSI, 'Stock' :Stock, 'MCAD': MCAD, 'info_': info_}

    return templates.TemplateResponse("output.html", content)

@router.delete("/delete")
def get_delete_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})