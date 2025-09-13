from rest_framework import serializers
from users.models import User,Order
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model=User
        fields=['first_name','last_name','email','bio','location','phone_number','password']

class UserSerializer(BaseUserSerializer):
    profile_image=serializers.ImageField()
    cover_photo=serializers.ImageField()
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'CustomUser'
        model=User
        fields=['id','first_name','last_name','email','bio','location','phone_number','profile_image','cover_photo']

class SimpleUserViewSerializer(BaseUserCreateSerializer):
    full_name=serializers.SerializerMethodField(method_name='user_full_name')
    class Meta(BaseUserCreateSerializer.Meta):
        model=User
        fields=['id','first_name','last_name','full_name']
    
    def user_full_name(self, user):
        return user.get_full_name()

class UserImageSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model=User
        fields=['id','profile_image','cover_photo']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','user', 'package_name', 'status', 'created_at', 'price']
        read_only_field=['id','user','created_at']

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','user', 'package_name', 'status', 'created_at', 'price']
        read_only_fields=['id','user', 'package_name', 'status', 'created_at', 'price']