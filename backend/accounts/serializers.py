from statistics import median_low
from urllib import request
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User 
from rest_framework import serializers
from django.conf import settings

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        
        # Add custom fields
        data['id'] = user.pk
        data['first_name'] = user.first_name
        data['last_name'] = user.last_name
        data['phone_number'] = str(user.phone_number)
        request = self.context['request']
        media_path = settings.MEDIA_URL.strip('/')
        data['profile_pic'] = f'{request.scheme}://{request.get_host()}/{media_path}/{str(user.profile_pic)}'
        data['email'] = user.email
        data['two_factor_active'] = user.two_factor_active

        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name','last_name','phone_number', 'email', 'password' )
        extra_kwargs = {'password': {'write_only': True},}

    def create(self, validated_data):
        return User.objects.create_inactive_user(**validated_data)

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name','last_name', 'phone_number')

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        return super(UserUpdateSerializer, self).update(instance, validated_data)

class UserPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','profile_pic')

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        return super(UserPictureSerializer, self).update(instance, validated_data)
