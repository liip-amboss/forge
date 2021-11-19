from django.urls import path
from . import views
from . import twofactor_views

urlpatterns = [
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(
        'token/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'
    ),
    path('activate-2fa/', twofactor_views.Activate2FA.as_view(), name='activate-2fa'),
    path(
        'deactivate-2fa/',
        twofactor_views.Deactivate2FA.as_view(),
        name='deactivate-2fa',
    ),
    path('2fa-url/', twofactor_views.Get2FAUrl.as_view(), name='2fa-url'),
    path(
        'reset-password/email/', views.ResetPasswordEmail.as_view(), name='reset-email'
    ),
    path('reset-password/check-token/', views.CheckToken.as_view(), name='check-token'),
    path('reset-password/reset/', views.ResetPassword.as_view(), name='reset'),
]
