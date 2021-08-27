import pyotp as pyotp
from django.http import HttpResponseBadRequest
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from . import serializers
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        operation_summary='Retrieve JWT', tags={'JSON Web Token'}
    ),
)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']

        authenticate_kwargs = {
            'email': email,
            'password': password,
        }

        user = authenticate(**authenticate_kwargs)

        if not user:
            raise AuthenticationFailed('No active account found')

        if not user.two_factor_active:
            return super(CustomTokenObtainPairView, self).post(request, *args, **kwargs)
        elif 'token' in request.data and request.data['token']:
            verified = pyotp.TOTP(user.two_factor_secret).verify(request.data['token'])
            if verified:
                return super(CustomTokenObtainPairView, self).post(request, *args, **kwargs)
            raise AuthenticationFailed('otp token is not verified')

        return Response(status=204)


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
