from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from accounts.models import CustomUser
from django.contrib.auth.models import Permission

class UserLoginSerializer(serializers.Serializer):
    '''Validates regular user login and returns auth token if active and user'''
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            if not user.role or user.role.name.lower() != 'user':
                raise serializers.ValidationError("Not a regular user account.")
            token, _ = Token.objects.get_or_create(user=user)
            return {
                'token': token.key,
                'username': user.username,
                'role': user.role.name,
            }
        raise serializers.ValidationError("Invalid credentials.")


class AdminLoginSerializer(serializers.Serializer):
    '''Validates admin login and returns auth token if active and admin'''
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            if not user.role or user.role.name.lower() != 'admin':
                raise serializers.ValidationError("Not an admin account.")
            token, _ = Token.objects.get_or_create(user=user)
            return {
                'token': token.key,
                'username': user.username,
                'role': user.role.name,
            }
        raise serializers.ValidationError("Invalid credentials.")
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename', 'content_type']

from .models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']