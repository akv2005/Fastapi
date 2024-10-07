import data_download as dd
import data_plotting as dplt

def main(ticker, period, start_date):
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    threshold = 20
    while True:

        stock_data = dd.fetch_stock_data(ticker, period, start_date)

        # Проверка наличия данных о акции
        if stock_data.empty:
            print(f"Нет данных для тикера '{ticker}'. Пожалуйста, проверьте правильность введенного тикера и запрашиваемого перода времени")

            break  # Возврат к началу цикла для повторного ввода


        # Добавление скользящего среднего, RSI, MACD
        stock_data = dd.add_moving_average(stock_data) # Добавляем расчет Скользящего среднего
        stock_data = dd.calculate_rsi(stock_data)  # Добавляем расчет RSI
        stock_data = dd.calculate_macd(stock_data)  # Добавляем расчет MACD
        print(stock_data,'stock_data')

        # Отрисовка графика и сохранение БД в csv-файл
        dplt.create_and_save_plot(stock_data, ticker, period)
        dplt.export_data_to_csv(stock_data, f'{ticker}_{period}')
        print(dd.calculate_and_display_average_price(stock_data))

        # Расчет процента колебаний
        if dd.notify_if_strong_fluctuations(stock_data, threshold) is not None:
            print(dd.notify_if_strong_fluctuations(stock_data, threshold))

        break  # Выход из цикла, если данные успешно получены


if __name__ == "__main__":
    main()
