from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from .views import CustomTokenObtainPairView

urlpatterns = [
    path('login', TokenObtainPairView.as_view()),
    path('refresh-session', TokenRefreshView.as_view()),
    path(
        'token-auth/',
        CustomTokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
]