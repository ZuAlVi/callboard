from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля

User = get_user_model()


class UserRegistrationSerializer(UserCreateSerializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100, allow_null=True, required=False)
    phone = serializers.CharField(max_length=25, allow_null=True, required=False)
    image = serializers.ImageField(allow_null=True, required=False)
    role = serializers.CharField(max_length=5)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            'password',
            'first_name',
            'last_name',
            'phone',
            'image',
            'role',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name', None),
            phone=validated_data.get('phone', None),
            image=validated_data.get('image', None),
            role=validated_data['role'],
        )
        return user


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'phone',
            'image',
            'role',
            'last_login',
            'is_active',
        )
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},
            'last_login': {'read_only': True},
        }
