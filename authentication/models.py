import jwt
import base64
from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    """
    Declare our own manager, redeclare user creation method
    """

    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Username needed!')

        if not email:
            raise ValueError('Email address needed!')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        """
        Returns newly created regular user.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Returns newly created admin user.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Admin must have is_staff field set to True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Admin must have is_superuser field set to True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Declaring our own class User basing on AbstractBaseUser and
    PermissionsMixin classes
    """

    username = models.CharField(db_index=True, max_length=32, unique=True)

    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False
        )

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    # Set email field for login
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('username',)

    # Set manager for User obj
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        """
        Generate JWT that lasts 30 days
        """
        dt = datetime.now() + timedelta(days=30)

        # urlsafe base64 encode key
        #secret = base64.urlsafe_b64encode(settings.SECRET_KEY)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
