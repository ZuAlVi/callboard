from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from users.apps import UserConfig
# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter

app_name = UserConfig.name

urlpatterns = [
]
