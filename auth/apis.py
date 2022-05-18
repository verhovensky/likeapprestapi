from urllib.parse import urlencode
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebTokenView
from django.conf import settings


from api.mixins import ApiErrorsMixin, PublicApiMixin, ApiAuthMixin

from users.services import user_record_login, user_get_or_create

from auth.services import jwt_login, google_get_user_info


class LoginApi(ApiErrorsMixin, ObtainJSONWebTokenView):
    def post(self, request, *args, **kwargs):
        # Reference: https://github.com/Styria-Digital/django-rest-framework-jwt/blob/master/src/rest_framework_jwt/views.py#L44
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.object.get('user') or request.user
        user_record_login(user=user)

        return super().post(request, *args, **kwargs)


class GoogleLoginApi(PublicApiMixin, ApiErrorsMixin, APIView):
    # TODO: serialize access_token in request.headers['Authorization']

    def get(self, request, *args, **kwargs):
        if not request.headers['Authorization']:
            return Response(content_type='application/json',
                            data={'error': 'No code specified'},
                            status=400)

        code = request.headers['Authorization']

        # TODO: if only access token = get user info, get_or_create, return jwt
        user_data = google_get_user_info(access_token=code)

        profile_data = {
            'email': user_data['email'],
            'first_name': user_data.get('given_name', ''),
            'last_name': user_data.get('family_name', ''),
            'picture': user_data.get('picture', ''),
            'email_verified': str(user_data.get('email_verified', '')),
        }

        user, _ = user_get_or_create(**profile_data)

        # TODO: return status 201 created = if created, 200 = if exists
        token = jwt_login(user=user)
        print(token)
        return Response(content_type='application/json',
                        status=200,
                        data={'token': token,
                              'profile': profile_data})


# TODO: logout on flutter = destroy token

# class LogoutApi(ApiAuthMixin, ApiErrorsMixin, APIView):
#     def post(self, request):
#         """
#         Logs out user by removing JWT cookie header.
#         """
#         user_change_secret_key(user=request.user)
#
#         response = Response(status=status.HTTP_202_ACCEPTED)
#         response.delete_cookie(settings.JWT_AUTH['JWT_AUTH_COOKIE'])
#
#         return response
