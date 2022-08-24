import pyotp as pyotp
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics 
from . import serializers
from .helpers import check_token
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate
from .models import User
from django.db import transaction


@method_decorator(
    name='put',
    decorator=swagger_auto_schema(
        operation_summary='Editing user firstname and lastname ', tags={"Users"}
    ),
)
class UpdateUserView(generics.UpdateAPIView):
    """
    This view change the user firstname and lastname in database.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserUpdateSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs ):
    
        instance = self.get_object()
        serializer= self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@method_decorator(
    name='put',
    decorator=swagger_auto_schema(
        operation_summary='Editing user picture', tags={"Users"}
    ),
)
class UpdateUserPicture(generics.UpdateAPIView):
    """
    This view change the user picture.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserPictureSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs ):
    
        instance = self.get_object()
        serializer= self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        operation_summary='Create a new user', tags={"Users"}
    ),
)
class UserRegisterView(generics.CreateAPIView):
    """
    This view creat a inactive user.
    """
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
                return super(CustomTokenObtainPairView, self).post(
                    request, *args, **kwargs
                )
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


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        operation_summary='Send reset password email', tags={'Reset password'}
    ),
)
class ResetPasswordEmail(APIView):
    """
    Sends the reset password email to the given email
    """

    def post(self, request, *args, **kwargs):
        if 'email' not in request.data:
            return Response(status=400, data='no email is specified')

        email = request.data['email']
        user = User.objects.filter(email=email).first()

        if user:
            user.reset_password(save=True)

        return Response(status=204)


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        operation_summary='Check if reset token is valid', tags={'Reset password'}
    ),
)
class CheckToken(APIView):
    """
    This view checks if the given token is a valid reset token
    """

    def post(self, request, *args, **kwargs):
        if 'token' not in request.data or 'email' not in request.data:
            return Response(status=400)

        token = request.data['token']
        email = request.data['email']

        valid = check_token(
            User.objects.filter(reset_token=token, email=email).first(), token
        )

        return Response(status=200, data={'valid': valid})


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        operation_summary='Reset the password', tags={'Reset password'}
    ),
)
class ResetPassword(APIView):
    """
    This view resets the password for the user
    """

    error_messages = {
        'no_token': 'no token is specified',
        'no_password': 'no password is specified',
        'no_email': 'no email is specified',
    }

    def post(self, request, *args, **kwargs):
        if 'token' not in request.data:
            return Response(status=400, data=self.error_messages['no_token'])
        if 'password' not in request.data:
            return Response(status=400, data=self.error_messages['no_password'])
        if 'email' not in request.data:
            return Response(status=400, data=self.error_messages['no_email'])

        token = request.data['token']
        email = request.data['email']
        user_with_token = User.objects.filter(reset_token=token, email=email).first()
        if not check_token(user_with_token, token):
            return Response(status=400, data='token is invalid')

        password = request.data['password']
        try:
            validate_password(password)
        except ValidationError as error:
            return Response(status=400, data=str(error))

        user_with_token.set_password(password)
        user_with_token.reset_token = None
        user_with_token.reset_salt = None
        user_with_token.save()

        return Response(status=204)
