import matplotlib.pyplot as plt
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')


def create_and_save_plot(data, ticker, period, filename=None):
    st_data = (data['begin'])[0]
    plt.style.use('seaborn-v0_8-dark-palette')
    plt.figure(figsize=(14, 10))

    if 'begin' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['begin']):
            data['begin'] = pd.to_datetime(data['begin'])
        plt.plot(data['begin'], data['close'], label='Close Price')
        plt.plot(data['begin'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel(f"Начальная дата {st_data}")
    plt.ylabel("Цена")
    plt.legend()
    plt.tight_layout()
    if filename is None:
        filename = f"./static/{ticker}_{period}_stock_price_chart.png"
    plt.savefig(filename)
    logging.info(f"График сохранен как {filename}")


    # График RSI
    plt.figure(figsize=(16, 10))
    plt.plot(data['begin'], data['RSI'], label='RSI', color='blue')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green')
    plt.title(f"RSI для {ticker}")
    plt.xlabel(("Дата"))
    plt.ylabel("RSI")
    plt.legend()
    plt.savefig(f"./static/{ticker}_{period}_RSI.png")
    logging.info(f"График RSI сохранен как {ticker}_{period}_RSI_chart.png")

    # График MACD
    plt.figure(figsize=(16, 10))
    plt.plot(data['begin'], data['MACD'], label='MACD', color='blue')
    plt.plot(data['begin'], data['Signal'], label='Signal Line', color='orange')
    plt.title(f"MACD для {ticker}")
    plt.xlabel("Дата")
    plt.ylabel("MACD")
    plt.legend()
    plt.savefig(f"./static/{ticker}_{period}_MACD.png")
    logging.info(f"График MACD сохранен как {ticker}_{period}_MACD_chart.png")

    plt.figure(figsize=(16, 10))
    plt.plot(data['begin'], data['close'], label='Close Price')
    plt.fill_between(data['begin'],
                     data['close'] - data['Std_Dev'],
                     data['close'] + data['Std_Dev'],
                     color='gray', alpha=0.3, label='Std Dev')
    plt.title(f"Стандартное отклонение для {ticker}")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()
    plt.savefig(f"./static/{ticker}_{period}_std_dev_chart.png")
    logging.info(f"График стандартного отклонения сохранен как {ticker}_{period}_std_dev_chart.png")


def export_data_to_csv(data, filename):
    """
    :param data: Принимает на вход DataFraim
    :param filename: имя для записи файла
    :return: Создает csv файл с БД, созданной в результате работы программы
    """
    logging.info(f"Таблица сохраена как {filename}.csv")
    return data.to_csv(f'./static/{filename}.csv')

# def export_data_to_html(data, filename):
#     """
#     :param data: Принимает на вход DataFraim
#     :param filename: имя для записи файла
#     :return: Создает html файл с БД, созданной в результате работы программы
#     """
#     frame = pd.DataFrame(np.arange(4).reshape(2, 2))
#     logging.info(f"Таблица сохраена как {filename}.html")
#     return frame.to_html(f'./static/{filename}.html')
