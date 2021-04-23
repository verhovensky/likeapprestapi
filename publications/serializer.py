from rest_framework import serializers
from .models import Publication
from authentication.models import User


class PublicationSerializer(serializers.ModelSerializer):
    #author_name = serializers.StringRelatedField(many=False)

    author = serializers.PrimaryKeyRelatedField(
        many=False,
        #default=serializers.CurrentUserDefault(),
        queryset=User.objects.all())

    class Meta:
        model = Publication
        fields = ('pk', 'title', 'content', 'created', 'author')
