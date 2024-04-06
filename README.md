# ADS-ONLINE 🛒📣

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django Version](https://img.shields.io/badge/Django-4.1-092E20.svg)](https://www.djangoproject.com/)

ADS-ONLINE - это полнофункциональный веб-сайт онлайн-магазина, включающий в себя frontend и backend части.

## 🔍 Backend

Backend часть проекта предполагает реализацию следующего функционала:

- 🔐 Авторизация и аутентификация пользователей
- 👤 Распределение ролей между пользователями (пользователь и админ)
- 📝 CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои)
- 💬 Под каждым объявлением пользователи могут оставлять отзывы

## 🚀 Установка и запуск

1. Клонировать проект:

```bash
git clone git@github.com:ZuAlVi/callboard.git
```

2. Установить зависимости:

```bash
pip install -r requirements.txt
```

3. Создать файл .env в корне проекта и внести необходимые данные, взяв за пример файл .env.example.

4.Провести миграции:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Запустить локальный сервер:
```bash
python3 manage.py runserver
```
