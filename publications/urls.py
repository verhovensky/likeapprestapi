from publications.views import PublicationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PublicationViewSet, basename='')

urlpatterns = router.urls
app_name = 'publications'
