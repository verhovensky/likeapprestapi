from django.urls import re_path
from authentication.views import RegistrationAPIView, LoginAPIView, UserViewSet

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    re_path(r'^users/?$', UserViewSet.as_view(), name='users_list')
]