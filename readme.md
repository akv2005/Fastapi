Общий обзор

Этот проект предназначен для загрузки исторических данных об акциях и их визуализации на веб-фреймворке FastAPI. Он использует библиотеку apimoex для получения данных и matplotlib для создания графиков.
 Пользователи могут выбирать различные тикеры и временные периоды для анализа, а также просматривать движение цен и скользящие средние на графике.

Структура и модули проекта

1.   main.py:
- В нем импортируеся веб-фреймворк FastAPI и Jinja2Templates для вывода  главной страницы.
Подключение папки static и /pages/router.py

2.   /pages/router.py 
- отвечает за выдачу HTML-страниц. В нем импортируеся веб-фреймворк FastAPI и Jinja2Templates для отрисовки страниц

 
3.   Папка static 
- В эту папку сохраняются графики и файл в формате csv, в которой находятся данные архивные данные эмитента за выбранный период

4.   Папка temlates 
- в этой папке находятся HTML страницы
   base.html - Главная страница входа.
   index.html - - Запрашивает у пользователя тикер акции и временной период, загружает данные, обрабатывает их и выводит результаты в виде графика.
   output.html - Страница вывода
   output_error.html -Страница вывода при некорректном вводе тикера

5. moex.py:

- Является точкой входа в программу работы данными биржи.

- Запрашивает у пользователя тикер акции и временной период, загружает данные, обрабатывает их и выводит результаты в виде графика.


6. data_download.py:

- Отвечает за загрузку данных об акциях.

- Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего.


3. data_plotting.py:

- Отвечает за визуализацию данных.

- Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.



Описание функций



1. data_download.py:

- fetch_stock_data(ticker, period): Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.

- add_moving_average(data, window_size): Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.

- calculate_and_display_average_price(data): Рассчитывает среднюю цену закрытия акций за заданный период.

- notify_if_strong_fluctuations(data, threshold=20): Анализирует данные и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период.

- calculate_rsi(data, window=14): Рассчитывает индекс относительной силы (RSI) для данных о ценах акций.

- calculate_macd(data, short_window=12, long_window=26, signal_window=9):  Рассчитывает Moving Average Convergence Divergence (MACD) для данных о ценах акций.


2. moex.py:

- main(): Основная функция, управляющая процессом загрузки, обработки данных и их визуализации. 
Запрашивает у пользователя ввод данных, вызывает функции загрузки и обработки данных, а затем передаёт результаты на визуализацию.



3. data_plotting.py:

- create_and_save_plot(data, ticker, period, filename): Создаёт график, отображающий цены закрытия и скользящие средние. Предоставляет возможность сохранения графика в файл. Параметр filename опционален; если он не указан, имя файла генерируется автоматически.
- export_data_to_csv(data, filename): Cоздает csv файл с таблицей по запрошенной акции и периоду. имя файла состоитт из названия акции и временного отрезка


Пошаговое использование

1. Открываете веб-страницу http://31.148.3.41:8088/ Входите в страницу ввода тикера

2. Введите интересующий вас тикер акции (например, 'GAZP' для Газпрома).

3. Введите начальнуя дату 

4. Введите желаемый временной период для анализа (например, '31' для данных за один месяц).

5. Программа обработает введённые данные, загрузит соответствующие данные об акциях, рассчитает скользящее среднее, отобразит график и выведет среднюю цену закрытия акций в консоль, 
и выведет графики на HTML станицу. 
