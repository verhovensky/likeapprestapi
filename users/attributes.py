from django.db import models


class City(models.TextChoices):
    MOSCOW = 'MSK'
    SAINT_PETERSBURG = 'PITER'
    NOVOSIBIRSK = 'NOVOSIB'
    EKATERINBURG = 'EKAT'
    KAZAN = 'KAZAN'
    NIZHNIY_NOVGOROD = 'NIZHNIYNOV'
    CHELYABINSK = 'CHELYAB'
    SAMARA = 'SAMARA'
    OMSK = 'OMSK'
    ROSTOV = 'ROSTOV'
    YFA = 'YFA'
    KRASN = 'KRASNOYARSK'
    VORON = 'VORONESH'
    PERM = 'PERM'
    VOLGOGRAD = 'VOLGOGRAD'


class Gender(models.TextChoices):
    MALE = 'M'
    FEMALE = 'F'
