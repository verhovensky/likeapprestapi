from rest_framework import serializers
from .models import Publication, UserPublicationRelation
from users.models import User


class PublicationSerializer(serializers.ModelSerializer):
    total_likes = serializers.ReadOnlyField()
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Publication
        fields = ('__all__')


class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPublicationRelation
        fields = ('publication', 'like', 'bookmarked')
