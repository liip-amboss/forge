from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from . import serializers
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        operation_summary='Retrieve JWT', tags={'JSON Web Token'}
    ),
)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        operation_summary='Refresh JWT', tags={'JSON Web Token'}
    ),
)
class CustomTokenRefreshView(TokenRefreshView):
    """
    This view returns a valid access token, if a valid refresh token is given.
    """

    serializer_class = TokenRefreshSerializer
