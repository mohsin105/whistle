from rest_framework import serializers
from users.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','email','bio','location','phone_number','password']