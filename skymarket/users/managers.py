from django.contrib.auth.models import (
    BaseUserManager
)


# TODO здесь должен быть менеджер для модели Юзера.
# TODO Поищите эту информацию в рекомендациях к проекту
class UserManager(BaseUserManager):
    """ Класс создания пользователя"""

    def create_user(self, email, first_name, password, last_name=None, phone=None, image=None):
        """Функция создания пользователя — в нее мы передаем обязательные поля"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role='user',
            image=image
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, password, last_name=None, phone=None, image=None):
        """
        функция для создания суперпользователя — с ее помощью мы создаем админинстратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role='admin',
            image=image
        )

        user.is_active = True

        user.save(using=self._db)

        return user
