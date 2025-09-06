from rest_framework import serializers
from users.models import User
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