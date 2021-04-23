import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
# jwt exceptions
from jwt import exceptions as jwtexceptions
from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Bearer'

    def authenticate(self, request):
        """
        1) `None` - We return `None` if we do not wish to authenticate. Usually
                    this means we know authentication will fail.

        2) `(user, token)` - We return a user/token combination when
                             authentication is successful.

         If neither case is met - raise the `AuthenticationFailed`
        """
        request.user = None

        # `auth_header` should be an array with two elements: 1) the name of
        # the authentication header (in this case, "Token") and 2) the JWT
        # that we should authenticate against.
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            # Invalid token header. No credentials provided. Do not attempt to
            # authenticate.
            return None

        elif len(auth_header) > 2:
            # Invalid token header. The Token string should not contain spaces.
            # Do not attempt to authenticate.
            return None

        # get an error if we didn't decode these values.
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            # The auth header prefix is not what we expected. Do not attempt to authenticate.
            return None

        # Pass credentials authentication to the method below.
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
        Try to authenticate the given credentials. If authentication is
        successful, return the user and token. If not, throw an error.
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except exceptions.AuthenticationFailed:
            msg = 'Authentication Failed. Could not decode token.'
            raise exceptions.AuthenticationFailed(msg)
        except jwtexceptions.InvalidSignatureError:
            msg = 'Invalid signature'
            raise jwtexceptions.InvalidSignatureError(msg)
        except jwtexceptions.DecodeError as e:
            msg = 'JWT token decode error'
            raise jwtexceptions.DecodeError(msg, e)
        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)

        return user, token
