from users.models import User
from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=64, verbose_name='Title')
    content = models.TextField(max_length=1200, verbose_name='Content')
    author = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked', through='UserPublicationRelation')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.title


class UserPublicationRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    bookmarked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return f'User: {self.user} Publication ID: {self.publication_id}'
