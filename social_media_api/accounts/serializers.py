from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Get the custom user model properly
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create user using the create_user method to hash the password
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Create a token for the user immediately upon registration
        Token.objects.create(user=user)
        return user
