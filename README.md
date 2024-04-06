# ADS-ONLINE 🛒📣

[![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django Version](https://img.shields.io/badge/Django-3.2-092E20.svg)](https://www.djangoproject.com/)
[![DRF Version](https://img.shields.io/badge/DRF-3.13-092E20.svg)](https://www.djangoproject.com/)

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
python3 skymarket/manage.py makemigrations
python3 skymarket/manage.py migrate
```
5. Запустить локальный сервер:
```bash
python3 skymarket/manage.py runserver
```
