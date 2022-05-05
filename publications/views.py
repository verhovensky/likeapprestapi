from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from authentication.backend import JWTAuthentication
from .serializer import PublicationSerializer
from likeapp.mixin import LikedMixin

from .models import Publication


class PublicationViewSet(viewsets.ModelViewSet,
                         LikedMixin):
    authentication_classes = ((JWTAuthentication,))
    permission_classes = [permissions.IsAuthenticated]
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def list(self, request, *args, **kwargs):
        serializer_class = PublicationSerializer(self.queryset, many=True,
                                                 context={"user": request.user})
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        single_publication = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PublicationSerializer(single_publication, context={"user": request.user})
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        pub_data = self.request.data
        serializer_class = PublicationSerializer(data={"title": pub_data['title'],
                                                       "content": pub_data['content'],
                                                       "author": self.request.user.pk})
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        headers = self.get_success_headers(serializer_class.data)
        return Response(serializer_class.data, status=status.HTTP_201_CREATED, headers=headers)
