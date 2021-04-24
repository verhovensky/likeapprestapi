from .models import Like
from .serializers import LikeSerializer
from django_filters import rest_framework as filters
from rest_framework import generics


class DateLikeSet(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    # fromdate = filters.DateFilter(name='created_at', lookup_expr='lte')
    # todate = filters.DateFilter(name='created_at', lookup_expr='gte')
    #
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('category', 'in_stock')
    #
    # class Meta:
    #     model = Like
    #     fields = 'created_at'
