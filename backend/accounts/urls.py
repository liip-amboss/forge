from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r'user', views.UserViewSet, basename='user')


urlpatterns = [
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(
        'token/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'
    ),
]
