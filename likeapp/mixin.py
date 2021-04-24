from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import add_like, remove_like
from django.shortcuts import get_object_or_404


class LikedMixin:
    @action(detail=True, methods=['POST'],
            permission_classes=['IsAuthenticated'])
    def like(self, request, pk=None):

        obj = get_object_or_404(self)
        add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'],
            permission_classes=['IsAuthenticated'])
    def unlike(self, request, pk=None):
        obj = get_object_or_404(self)
        remove_like(obj, request.user)
        return Response()
