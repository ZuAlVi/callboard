# Generated by Django 3.2.6 on 2024-04-04 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20240326_1739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Коммантарии'},
        ),
    ]
