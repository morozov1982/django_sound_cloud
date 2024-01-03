from django.conf import settings

from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.exceptions import AuthenticationFailed

from src.oauth.models import AuthUser
from src.oauth import serializers
from src.oauth.services import basic_auth


def check_google_auth(google_user: serializers.GoogleAuthSerializer) -> dict:
    try:
        id_token.verify_oauth2_token(
            google_user['token'], requests.Request(), settings.GOOGLE_CLIENT_ID)
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad Google token')

    user, ddd = AuthUser.objects.get_or_create(email=google_user['email'])
    return basic_auth.create_token(user.id)
