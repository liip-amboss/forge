from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
