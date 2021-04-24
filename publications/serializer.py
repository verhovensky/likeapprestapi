from rest_framework import serializers
from .models import Publication
from likeapp.utils import is_liked
from authentication.models import User


class PublicationSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    author = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=User.objects.all())

    class Meta:
        model = Publication
        fields = ('pk',
                  'title',
                  'content',
                  'created',
                  'author',
                  'total_likes',
                  'is_liked')

    def get_is_liked(self, obj) -> bool:
        user = self.context.get('user')
        return is_liked(obj, user)
