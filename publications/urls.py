from publications.views import PublicationViewSet, PublicationRelationView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PublicationViewSet, basename='publication')
router.register(r'relations', PublicationRelationView, basename='relation')

urlpatterns = router.urls
app_name = 'publications'
