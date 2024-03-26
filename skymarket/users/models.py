from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
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


class User(AbstractBaseUser, PermissionsMixin):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту

    email = models.EmailField(unique=True, max_length=150, verbose_name='Email')

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    phone = models.CharField(max_length=25, verbose_name='Телефон', **NULLABLE)
    image = models.ImageField(upload_to='user/', verbose_name='Фото', **NULLABLE)

    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)

    last_login = models.DateTimeField(default=timezone.now, verbose_name='Последняя авторизация')

    is_active = models.BooleanField(default=True, verbose_name='Активный')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
