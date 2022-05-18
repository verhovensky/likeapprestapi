from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import AnonymousUser
from rest_framework import exceptions


class JwtAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        try:
            authenticated = JSONWebTokenAuthentication().authenticate(request)
            if authenticated:
                request.user = authenticated[0]
            else:
                request.user = AnonymousUser
        except exceptions.AuthenticationFailed as err:
            print(err)
            request.user = AnonymousUser
        return response
