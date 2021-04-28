from likeapprest.settings import TIME_ZONE
from django.core.cache import cache
from .backend import JWTAuthentication
import datetime
import pytz

tz = pytz.timezone(TIME_ZONE)
auth = JWTAuthentication()


class UpdateLastActivityMiddleware(object):
    def process_view(self, request, token, view_args, view_kwargs):
        assert hasattr(request, 'user'), \
            'The UpdateLastActivityMiddleware requires authentication middleware to be installed.'
        try:
            a = auth.authenticate(request=request)
            user_data = {}
            user_data.update({'name': a[0].username,
                              'time': str(datetime.datetime.now(tz=tz)),
                              'endpoint': request.path})
            cache.get_or_set(user_data['name'], user_data)
        # no exceptions occur yet, let it be here nevertheless
        except TypeError as e:
            pass
            # raise TypeError('No data') from e

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
