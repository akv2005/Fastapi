import matplotlib.pyplot as plt
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')


def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

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
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()
    plt.tight_layout()


    # График RSI
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['RSI'], label='RSI', color='blue')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green')
    plt.title(f"RSI для {ticker}")
    plt.xlabel("Дата")
    plt.ylabel("RSI")
    plt.legend()
    plt.savefig(f"./static/{ticker}_{period}_RSI.png")
    logging.info(f"График RSI сохранен как {ticker}_{period}_RSI_chart.png")

    # График MACD
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['MACD'], label='MACD', color='blue')
    plt.plot(data.index, data['Signal'], label='Signal Line', color='orange')
    plt.title(f"MACD для {ticker}")
    plt.xlabel("Дата")
    plt.ylabel("MACD")
    plt.legend()
    plt.savefig(f"./static/{ticker}_{period}_MACD.png")
    logging.info(f"График MACD сохранен как {ticker}_{period}_MACD_chart.png")


    if filename is None:
        filename = f"./static/{ticker}_{period}_stock_price_chart.png"
    plt.savefig(filename)
    logging.info(f"График сохранен как {filename}")
def export_data_to_csv(data, filename):
    """

    :param data: Принимает на вход DataFraim
    :param filename: имя для записи файла
    :return: Создает csv файл с БД, созданной в результате работы программы
    """
    logging.info(f"Таблица сохраена как {filename}.csv")
    return data.to_csv(f'./static/{filename}.csv')

