from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ads.models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class AdSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    author_id = serializers.IntegerField(source='author.id')
    phone = serializers.CharField(source='author.phone')

    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'phone', 'description', 'author_first_name', 'author_last_name', 'author_id']


class AdDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)
        ad.author = self.context['request'].user
        ad.save()
        return ad


class CommentDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        obj_pk = self.context['view'].kwargs['ad_pk']
        obj_com = Ad.objects.get(pk=obj_pk)

        if not 'text' in validated_data:
            raise ValidationError('Вы забыли написать комментарий')
        comm = Comment.objects.create(**validated_data)
        comm.author = self.context['request'].user
        comm.ad = obj_com
        comm.save()
        return comm
