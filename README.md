# weather_bot


Задача: умный сервис прогноза погоды,
уровень сложности средний

В чат-боте пользователь указывает свое местоположение, программа с помощью библиотеки geopy определяет наиболее похожий на текст город и возвращает его координаты. По координатам с помощью библиотеки pyowm получается информация о текущей погоде, в ответ пользователю возвращается текст в формате "{Определенное местоположение}: {погодные условия на улице}, температура - ___", в случае, если пользователь отправил смайлик, ему в ответ приходит он же :)

Для запуска: положить токены для телеграм-бота и https://openweathermap.org/ на отдельных строках в tokens.txt

Установить необходимые библиотеки и запустить основной скрипт: 
```
pip install -r requirements.txt
python weather_bot.py
```


Ссылка на видео с работой чат-бота: https://yadi.sk/i/8Yqspuvb1lXhXQ
