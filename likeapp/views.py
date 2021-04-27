from .models import Like
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

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        from_date = self.request.data['from']
        to_date = self.request.data['to']
        queryset_f = Like.objects.filter(created_at__range=(from_date, to_date))
        serializer_class = LikeSerializer(queryset_f, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
