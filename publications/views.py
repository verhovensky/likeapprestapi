from rest_framework import viewsets, permissions
from rest_framework.mixins import UpdateModelMixin
from authentication.backend import JWTAuthentication
from .serializer import PublicationSerializer, RelationSerializer
from django.db.models import Count
from .models import Publication, UserPublicationRelation


class PublicationViewSet(viewsets.ModelViewSet):
    authentication_classes = ((JWTAuthentication,))
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PublicationSerializer
    queryset = Publication.objects.annotate(total_likes=Count('likes'))
    # TODO: add filtering and ordering
    # search_fields =
    # filter_fields =
    # ordering_fields =

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()


class PublicationRelationView(viewsets.GenericViewSet,
                              UpdateModelMixin):
    queryset = UserPublicationRelation.objects.all()
    authentication_classes = ((JWTAuthentication,))
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RelationSerializer
    lookup_field = 'publication'

    def get_object(self):
        # IntegrityError on ForeignConstraint failed (500)
        obj, _ = UserPublicationRelation.objects.get_or_create(
            user=self.request.user,
            publication_id=self.kwargs['publication']
        )
        return obj
