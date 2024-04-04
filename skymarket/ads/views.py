from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import get_object_or_404
from ads.paginations import DefaultPagination
from ads.serializers import *


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdListCreateAPIView(generics.ListCreateAPIView):
    """
    При GET-запросе класс возвращает все объявления
    При POST-запросе класс создает объявление
    """

    serializer_class = AdDefaultSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination


class MyAdListAPIView(generics.ListAPIView):
    """Класс возвращает список объявлений текущего пользователя"""

    serializer_class = AdDefaultSerializer
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class AnotherAdRetrieveAPIView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    При GET-запросе возвращает объявление по id
    При PUTCH-запросе редактирует объявление по id
    При DEL-запросе удаляет объявление по id
    """

    serializer_class = AdSerializer
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    queryset = Ad.objects.all()
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if (self.request.user != obj.author) or (self.request.user.role != 'admin'):
            raise ValidationError('У вас нет на это прав на это действие!')

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if (self.request.user != obj.author) or (self.request.user.role != 'admin'):
            raise ValidationError('У вас нет на это прав на это действие!')

        return super().destroy(request, *args, **kwargs)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    """
    При GET-запросе возвращает список всех коментариев к объявлению
    При POST-запросе создает новый коментарий
    """
    serializer_class = CommentDefaultSerializer
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination

    def get_queryset(self):
        return Comment.objects.filter(ad=self.kwargs['ad_pk'])


class AnotherCommentRetrieveAPIView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    При GET-запросе возвращает комментарий по его id
    При PATCH-запросе редактирует комментарий по его id
    При DEL-запросе удаляет комментарий по его id
    """
    serializer_class = CommentDefaultSerializer
    queryset = Comment.objects.all()
    pagination_class = IsAuthenticated

    def get_object(self):
        ad_pk = self.kwargs.get('ad_pk')
        comment_id = self.kwargs.get('id')
        return get_object_or_404(Comment, pk=comment_id, ad=ad_pk)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if (self.request.user != obj.author) or (self.request.user.role != 'admin'):
            raise ValidationError('У вас нет на это прав на это действие!')

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if (self.request.user != obj.author) and (self.request.user.role != 'admin'):
            raise ValidationError('У вас нет на это прав на это действие!')

        return super().destroy(request, *args, **kwargs)
