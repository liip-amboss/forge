from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, JSONParser
from . import serializers
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from .models import User
from .serializers import UserSerializer


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


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = IsAuthenticated
    parser_classes = [MultiPartParser, JSONParser]

    @action(methods=['PATCH'], detail=True, url_path='image', url_name='image')
    def upload_image(self, request, pk):
        print(request.data)
        user = User.objects.get(pk=pk)
        user.image = request.data['image']
        user.save()
