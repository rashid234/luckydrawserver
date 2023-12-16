from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

User = get_user_model()

class UserRegister(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "email", "password2"]

    def validate(self, data):
        # Ensure that the password and password2 fields match
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        return data

    def create(self, validated_data):
        # Remove password2 from the validated data as it is not a model field
        validated_data.pop('password2', None)

        # Create and return the user instance
        user = User.objects.create_user(**validated_data)
        return user

class CustomAuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')

    user_id = serializers.SerializerMethodField()

    def get_user_id(self, obj):
        return obj.user.id