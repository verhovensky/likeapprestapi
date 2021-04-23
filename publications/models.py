from django.db import models
from authentication.models import User
# Create your models here.


# class Like(models.Model):
#     owner = models.OneToOneField(User, on_delete=models.SET('Deleted'))
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Created at")


class Publication(models.Model):
    title = models.CharField(max_length=64, verbose_name='Title')
    content = models.TextField(max_length=1200, verbose_name='Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    #like = models.ManyToManyField(Like, related_name='like', blank=True)

    def __str__(self):
        return self.title

    # def get_likes(self):
    #     return self.like.count()
