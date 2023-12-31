# Telegram DeepL Bot

Очень простой бот для телеграма, переводящий весь входящий в него текст с английского на русский. ID пользователя, оригинальный и переведенный текст записываются в базу данных на сервере.

# Установка и запуск

## С использованием Docker:

* Склонировать репозиторий
* Перейти в папку с репозиторием, вставить свои BOT_TOKEN (Токен телеграм бота) и DEEPL_AUTH_KEY (Ключ от АПИ DeepL) в файл **api.env**
* Вызвать команду 
```
docker-compose up
```
* Docker установит всё необходимое и запустит бота, для доступа к базе данных с историей запросов пользователей можно воспользоваться PgAdmin по адресу http://localhost:5050/ . В нем подключиться по данным, указанным в **docker-compose.yml** (обязательно ставьте хостнейм "db" при добавлении сервера в pgAdmin)

## Без использования Docker:

* Склонировать репозиторий
* Установить poetry и с помощью команды поставить все необходимые пакеты 
```
poetry install
```
* Изменить следующие данные сервера PostreSQL на свои: 
```
host="db"
database="test_db"
user="root"
password="root"
```
* Прописать свои BOT_TOKEN (Токен телеграм бота) и DEEPL_AUTH_KEY (Ключ от АПИ DeepL) в переменные среды
* Запустить бот с помощью команды
```
poetry run python bot.py
```

## Использование

Бот предельно прост - для перевода текста необходимо прислать ему сообщение на английском.