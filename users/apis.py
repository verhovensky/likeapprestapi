from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from api.mixins import ApiErrorsMixin, ApiAuthMixin, PublicApiMixin
from auth.services import jwt_login, google_validate_id_token
from users.services import user_get_or_create
from users.selectors import user_get_me
from users.models import User
from users.serializers import UserUpdateGetSerializer


class UserMeApi(ApiAuthMixin, ApiErrorsMixin, APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        serializer = UserUpdateGetSerializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        data = request.data
        qs = User.objects.get(pk=self.request.user.pk)
        serializer = UserUpdateGetSerializer(qs, data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

# TODO: PUT for user UPDATE params: token (check if user is authenticated)


class UserInitApi(PublicApiMixin, ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        first_name = serializers.CharField(required=False, default='')
        last_name = serializers.CharField(required=False, default='')

    def post(self, request, *args, **kwargs):
        id_token = request.headers.get('Authorization')
        google_validate_id_token(id_token=id_token)

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # We use get-or-create logic here for the sake of the example.
        # We don't have a sign-up flow.
        user, _ = user_get_or_create(**serializer.validated_data)

        response = Response(data=user_get_me(user=user))
        response = jwt_login(user=user)

        return response
