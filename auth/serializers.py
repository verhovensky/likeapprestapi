from rest_framework import serializers


class GoogleAccessTokenSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=500)
