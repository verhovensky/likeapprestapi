from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .models import Like
# import datetime
# Bishkek Time zone
# import pytz
# timezone = pytz.timezone("Asia/Bishkek")

User = get_user_model()


def add_like(obj, user):
    """Like `obj`.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    return like


def remove_like(obj, user):
    """Delete like from `obj`.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()


def is_liked(obj, user) -> bool:
    # auth ckeck?
    if not user:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    likes = Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return likes.exists()

# Validate input datetime passed in request.data


TIME_FORMATS = ['%Y-%m-%d',
                '%Y %m %d',
                '%Y-%m-%d %H',
                '%Y-%m-%d %H:%M',
                '%Y %m %d %H:%M',
                '%Y-%m-%d %H:%M']

# in case we need more precise statistics
# def is_valid_datetime(time):
#     if time is None:
#         return None
#     for time_format in TIME_FORMATS:
#         try:
#             obj_dt = datetime.datetime.strptime(time, time_format).astimezone(timezone)
#             day = obj_dt.date()
#             return day
#         except ValueError as e:
#             return e
