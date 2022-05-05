from .models import Like
from .serializers import LikeSerializer
from rest_framework.generics import ListAPIView
from rest_framework import status, permissions
from rest_framework.response import Response
from authentication.backend import JWTAuthentication
from django.core.exceptions import ValidationError


class LikesView(ListAPIView):
    authentication_classes = ((JWTAuthentication,))
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            from_date = self.request.GET['from']
            to_date = self.request.GET['to']
            queryset_f = Like.objects.filter(created_at__range=(from_date, to_date))
            serializer_class = LikeSerializer(queryset_f, many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except (ValidationError, KeyError):
            return Response('Date format should be YYYY-MM-DD', status=status.HTTP_400_BAD_REQUEST)
