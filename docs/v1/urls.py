import base64
from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.routers import DefaultRouter
from .views import UserCreateAPIView, MyTokenObtainPairView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('', TokenBlacklistView.as_view(), name='token_blacklist'),
]
urlpatterns += router.urls
