from likeapp.views import LikeSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LikeSet)

urlpatterns = router.urls
app_name = 'likeapp'
