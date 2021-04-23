from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from authentication.backend import JWTAuthentication
from .serializer import PublicationSerializer

from .models import Publication


class PublicationViewSet(viewsets.ModelViewSet):
    authentication_classes = ((JWTAuthentication,))
    permission_classes = [permissions.IsAuthenticated]
    #queryset = Publication.objects.all().order_by('created')
    serializer_class = PublicationSerializer

    def get_queryset(self):
        return Publication.objects.all()

    def create(self, request, *args, **kwargs):
        user = self.request.user
        pub_data = self.request.data
        serializer = self.get_serializer(data={"title": pub_data['title'],
                                               "content": pub_data['content'],
                                               "author": user.pk})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)