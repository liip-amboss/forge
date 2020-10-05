from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer
