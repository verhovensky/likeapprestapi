from .models import Like
from .utils import is_valid_date
from .serializers import LikeSerializer
from rest_framework.decorators import action
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from authentication.backend import JWTAuthentication


class LikeSet(viewsets.ModelViewSet):
    authentication_classes = ((JWTAuthentication,))
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()

    def list(self, request, *args, **kwargs):
        serializer_class = LikeSerializer(self.queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    # migrate this function to mixin.py
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        from_date = self.request.data['from']
        to_date = self.request.data['to']
        fd = is_valid_date(from_date)
        td = is_valid_date(to_date)
        queryset_f = Like.objects.filter(created_at__range=(fd, td))
        serializer_class = LikeSerializer(queryset_f, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
