from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .utils import add_like, remove_like, is_liked
from authentication.models import User
from publications.models import Publication

# The logic of these two methods can be simplified to be the one


class LikedMixin:
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        user_pk = request.user.pk
        user = get_object_or_404(User, pk=user_pk)
        obj = get_object_or_404(Publication, pk=pk)
        check_liked = is_liked(obj, user)
        if check_liked is True:
            return Response(status=status.HTTP_302_FOUND)
        else:
            add_like(obj, user)
            return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        user_pk = request.user.pk
        user = get_object_or_404(User, pk=user_pk)
        obj = get_object_or_404(Publication, pk=pk)
        check_liked = is_liked(obj, user)
        if check_liked is True:
            remove_like(obj, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
