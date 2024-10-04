from fastapi import APIRouter, Request, Form
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
    return templates.TemplateResponse("input.html", {"request": request})

@router.post("/postdata")
def postdata(ticker=Form(), period = Form()):
     stock_data = dd.fetch_stock_data(ticker, period)
     # Добавление скользящего среднего, RSI, MACD
     stock_data = dd.add_moving_average(stock_data)  # Добавляем расчет Скользящего среднего
     stock_data = dd.calculate_rsi(stock_data)  # Добавляем расчет RSI
     stock_data = dd.calculate_macd(stock_data)  # Добавляем расчет MACD
     print(stock_data, 'stock_data')

     # Отрисовка графика и сохранение БД в csv-файл
     dplt.create_and_save_plot(stock_data, ticker, period)
     dplt.export_data_to_csv(stock_data, f'{ticker}_{period}')
     print(dd.calculate_and_display_average_price(stock_data))

     # Расчет процента колебаний
#     if dd.notify_if_strong_fluctuations(stock_data, threshold) is not None:
#         print(dd.notify_if_strong_fluctuations(stock_data, threshold))
     return
