from rest_framework import serializers

from src.oauth.models import AuthUser, SocialLink


class UserSerializer(serializers.ModelSerializer):
    """Сериализация данных пользователя"""
    class Meta:
        model = AuthUser
        fields = ('avatar', 'country', 'city', 'bio', 'display_name')


class SocialLinkSerializer(serializers.ModelSerializer):
    """Сериализация ссылок соц. сетей"""
    # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SocialLink
        fields = ('id', 'link')


class AuthorSerializer(serializers.ModelSerializer):
    """Сериализация данных автора"""
    social_links = SocialLinkSerializer(many=True)

    class Meta:
        model = AuthUser
        fields = ('id', 'avatar', 'country', 'city', 'bio', 'display_name', 'social_links')


class GoogleAuthSerializer(serializers.Serializer):
    """Сериализация данных от Google"""
    email = serializers.EmailField()
    token = serializers.CharField()
