from django.db import models
from .attributes import City, Gender
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.core.management.utils import get_random_secret_key
from django.core.validators import RegexValidator


# TODO: test user creation

class MyUserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.apple = 'adminAPPLE'
        user.save(using=self._db)

        return user


class User(AbstractUser):
    username = None

    # TODO: necessary fields (
    #  phone, email, city, photos, visible, surname, gender, about, city, in_search) + apple_id_field
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,16}$',
                                 message="Макс. длинна = 16 знаков. Прим: +7987001122")
    phone = models.CharField(max_length=16, validators=[phone_regex],
                             blank=True, verbose_name="Телефон")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    about = models.CharField(max_length=1500, blank=True, default='', verbose_name='О себе')
    # photo = models.ImageField(upload_to='users/%Y/%m/%d', default='users/no-user-photo.jpg',
    #                           blank=True, verbose_name="Фото")
    created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    # TODO: city db_index ?
    city = models.CharField(max_length=128, choices=City.choices, verbose_name='Город',
                            default=City.MOSCOW)
    # TODO: searching redundant ? Perform lookups only by gender ?
    gender = models.CharField(max_length=128,
                              choices=Gender.choices,
                              verbose_name='Пол',
                              blank=True)
    searching = models.CharField(max_length=128,
                                 choices=Gender.choices,
                                 verbose_name='Ищу',
                                 blank=True)
    apple = models.CharField(max_length=128, blank=True, unique=True,
                             verbose_name='AppleID')
    visible = models.BooleanField(default=True, verbose_name='Видимый')
    email = models.EmailField(unique=True, db_index=True)
    secret_key = models.CharField(max_length=255, default=get_random_secret_key)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    @property
    def name(self):
        if not self.last_name:
            return self.first_name.capitalize()

        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'
