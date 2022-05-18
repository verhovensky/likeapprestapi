from rest_framework.serializers import ModelSerializer
from users.models import User


class UserUpdateGetSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['created', 'updated', 'apple', 'visible', 'password',
                   'email', 'secret_key', 'last_login', 'is_staff', 'is_superuser']
