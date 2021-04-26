from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(
        many=False)

    class Meta:
        model = Like
        fields = ('pk', 'user', 'created_at')
