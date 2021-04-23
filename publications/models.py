from django.contrib.contenttypes.fields import GenericRelation
from authentication.models import User
from likeapp.models import Like
from django.db import models
# Create your models here.


class Publication(models.Model):
    title = models.CharField(max_length=64, verbose_name='Title')
    content = models.TextField(max_length=1200, verbose_name='Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    likes = GenericRelation(Like)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()
