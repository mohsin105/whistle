from rest_framework import serializers
from users.models import User
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model=User
        fields=['first_name','last_name','email','bio','location','phone_number','password']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'CustomUser'
        model=User
        fields=['first_name','last_name','email','bio','location','phone_number','profile_image']