from django.urls import path
from . import views


urlpatterns = [
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(
        'token/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'
    ),
    path('reset-password/email/', views.ResetPasswordEmail.as_view(), name='reset-email'),
    path('reset-password/check-token/', views.CheckToken.as_view(), name='check-token'),
    path('reset-password/reset/', views.ResetPassword.as_view(), name='reset'),
]
