from likeapp.views import LikesView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

urlpatterns = [
    path('statistics/', LikesView.as_view()),
    path('', include(router.urls))
]

app_name = 'likeapp'
