# Контрольная работа 1

Технологии разработки серверных приложений
Студент: Доськова Мария Павловна
Группа: ЭФБО-03-24
Семестр: 4 семестр, 2025/2026 уч. год

## Инструкция по запуску
1. Клонировать репозиторий:

git clone https://github.com/mitjink/sadt_kr1  
cd 1_kr  

2. Создать и активировать виртуальное окружение:

### Windows
python -m venv venv  
venv\Scripts\activate

### Mac/Linux
python3 -m venv venv  
source venv/bin/activate

3. Установить зависимости:

pip install fastapi uvicorn pydantic

4. Запустить сервер:

uvicorn app:app --reload

5. Открыть в браузере:

Документация Swagger: http://localhost:8000/docs  

Корневой маршрут: http://localhost:8000/

## Задание 1.1

![1.1 - код и запуск в uvicorn](screenshots/1.jpg)
![1.1 - ответ в браузере](screenshots/2.jpg)
![1.1 - изменения в коде и autoreoad](screenshots/3.jpg)
![1.1 - ответ в браузере после изменений](screenshots/4.jpg)

## Задание 1.2

![1.2 - FileResponse](screenshots/5.jpg)
![1.2 - HTML в браузере](screenshots/6.jpg)

## Задание 1.3

![1.3 - код эндпоинта /calculate](screenshots/7.jpg)
![1.3 — тест post /calculate в Postman](screenshots/8.jpg)

## Задание 1.4

![1.4 — код эндпоинта /users](screenshots/9.jpg)
![1.4 — тест get /users в Postman](screenshots/10.jpg)

## Задание 1.5

![1.5 — код эндпоинта /user](screenshots/11.jpg)
![1.5 — тест get /user в Postman](screenshots/12.jpg)

## Задание 2.1

![2.1 — код для задания 2.1](screenshots/13.jpg)
![2.1 — тест в Postman](screenshots/14.jpg)

## Задание 2.2

![2.2 — код для задания 2.2](screenshots/15.jpg)
![2.2 — modals для 2.2](screenshots/16.jpg)
![2.2 — правильный запрос в Postman](screenshots/17.jpg)
![2.2 — пример ошибки валидации (message, символов меньше допустимого)](screenshots/18.jpg)
![2.2 — пример ошибки валидации (использование недопустимых слов)](screenshots/19.jpg)
![2.2 — пример ошибки валидации (name, символов меньше допустимого)](screenshots/20.jpg)