from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

NULLABLE = {'blank': True, 'null': True}

User = get_user_model()


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=100, default='Отдам', verbose_name='Название')
    price = models.IntegerField(default=0, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='ads/', verbose_name='Изображение', **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', **NULLABLE)
    text = models.TextField(verbose_name='Коментарий', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания', **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление', **NULLABLE)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коммантарии'
