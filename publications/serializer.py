from rest_framework import serializers
from .models import Publication
from authentication.models import User


class PublicationSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=User.objects.all())

    class Meta:
        model = Publication
        fields = ('pk', 'title', 'content', 'created', 'author', 'total_likes')
