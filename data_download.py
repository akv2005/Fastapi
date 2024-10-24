import requests
import apimoex
import logging
import pandas as pd
import datetime



logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')
def fetch_stock_data(ticker, period, start_date):
    security = ticker
    s_date = start_date  # Начальная дата
    end_date = datetime.datetime.today()  # Конечная дата
    interval = period  #'24'  Интервал: '
    with requests.Session() as session:
        stock = apimoex.get_board_candles(session, security=security, start=s_date, end=end_date, interval = interval)
        data = pd.DataFrame(stock)
        return data

def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    """
    :param data: Принимает БД с данными по запрошенной акции
    :return: Возвращает среднее значение колонки 'CLOSE'
    """
    avg = data['close'].mean(axis=0)
    logging.info(f'средняя цена закрытия акций: {avg}')
    return avg


def notify_if_strong_fluctuations(data, threshold):
    """
    :param data: Принимает БД с данными по запрошенной акции
    :param threshold: Принимает пороговое значение колебаний в процентах от средней цены цены закрытия за указанный период
    :return: Возвращает предупреждение, если цена закрытия акций за заданный перуд изменяется больше значения threshold
    """
    min_price = data['close'].min()
    max_price = data['close'].max()
    threshold = 20
    dif = max_price - min_price
    percent = dif / (calculate_and_display_average_price(data) / 100)
    print(f"min: {min_price}, max:{max_price}")
    if percent >= threshold:
        logging.warning(f'высокий уровень колебания акций!   {percent} %')
        return 'Компания не стабильна, будьте внимательны!'
    else:
        logging.info( f"уровень колебания эмитента  в пределах   {percent} %")
        return 'эмитент стабилен'



def calculate_rsi(data, window=14):
    """
    Рассчитывает индекс относительной силы (RSI) для данных о ценах акций.

    :param data: DataFrame с историческими данными о ценах акций
    :param window: Период расчета RSI
    :return: DataFrame с добавленным столбцом 'RSI'
    """
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    """
    Рассчитывает Moving Average Convergence Divergence (MACD) для данных о ценах акций.

    :param data: DataFrame с историческими данными о ценах акций
    :param short_window: Период для короткой экспоненциальной скользящей средней (EMA)
    :param long_window: Период для длинной экспоненциальной скользящей средней (EMA)
    :param signal_window: Период для сигнальной линии MACD
    :return: DataFrame с добавленными столбцами 'MACD' и 'Signal'
    """
    data['EMA_short'] = data['close'].ewm(span=short_window, adjust=False).mean()
    data['EMA_long'] = data['close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA_short'] - data['EMA_long']
    data['Signal'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    return data

def LastNlines(fname): # Формирует строку об средней цены за период и волатильности эмитента
    with open(fname) as file:
        ll = "*"
        lll = "..."
        for line in (file.readlines()[-2:]):
            ll = ll + 3*lll + line[line.find('|'):]
            print(ll, end ='')
    return ll

def calculate_and_display_std_dev(data):
    """
    Рассчитывает стандартное отклонение цен закрытия и добавляет его в DataFrame.

    :param data: DataFrame с историческими данными о ценах акций
    :return: DataFrame с добавленным столбцом 'Std_Dev'
    """
    std_dev = data['close'].std()
    data['Std_Dev'] = std_dev
    logging.info(f'Стандартное отклонение цен закрытия акций: {std_dev}')
    return data