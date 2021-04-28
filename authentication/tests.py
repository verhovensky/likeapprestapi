from django.test import TestCase
from django.core.cache import cache
from likeapprest.settings import TIME_ZONE
import datetime
import pytz

tz = pytz.timezone(TIME_ZONE)


class CacheTestCase(TestCase):
    def test_cache(self):
        cache.get_or_set('user', 'admin')
        cache.get_or_set('time', str(datetime.datetime.now(tz=tz)))
        cache.get_or_set('endpoint', '/users/1/')

        self.assertEqual(cache.get('user'), 'admin')
        self.assertEqual(cache.get('time'), str(datetime.datetime.now(tz=tz)))
        self.assertEqual(cache.get('endpoint'), '/users/1/')
