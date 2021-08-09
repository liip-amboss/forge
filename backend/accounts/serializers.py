from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from .models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        # Add custom fields
        data['id'] = user.pk
        data['first_name'] = user.first_name
        data['last_name'] = user.last_name
        data['email'] = user.email

        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'image', 'phone_number',)
