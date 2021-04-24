from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Like.objects.all())

    class Meta:
        model = Like
        fields = ('pk', 'content_object', 'user')
