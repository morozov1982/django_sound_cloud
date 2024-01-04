from rest_framework import serializers

from src.oauth.models import AuthUser


class UserSerializer(serializers.ModelSerializer):
    """Сериализация данных пользователя"""
    class Meta:
        model = AuthUser
        fields = ('avatar', 'country', 'city', 'bio', 'display_name')


class GoogleAuthSerializer(serializers.Serializer):
    """Сериализация данных от Google"""
    email = serializers.EmailField()
    token = serializers.CharField()
