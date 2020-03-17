import logging
from django.contrib.auth import get_user_model
from rest_framework import authentication


class AuthUserAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        log = logging.getLogger('django')
        log.debug(request.META)
        user_model = get_user_model()
        username = request.META.get('HTTP_AUTH_USER')
        if not username:
            return None
        user, created = user_model.objects.get_or_create(username=username)
        return user, None
