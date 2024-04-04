from django.contrib import admin

from ads.models import Ad, Comment


# TODO здесь можно подкючить ваши модели к стандартной джанго-админке

@admin.register(Ad)
class RelatedHabitAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'image', 'author')


@admin.register(Comment)
class RelatedHabitAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'ad')
