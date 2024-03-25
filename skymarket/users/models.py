from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    # TODO закончите enum-класс для пользователя
    USER = 'user', _('user')
    ADMIN = 'admin', _('admin')


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, max_length=150, verbose_name='Email')

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    phone = models.CharField(max_length=25, verbose_name='Телефон', **NULLABLE)

    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)

    last_login = models.DateTimeField(default=timezone.now, verbose_name='Последняя авторизация')

    is_active = models.BooleanField(default=True, verbose_name='Активный')

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



