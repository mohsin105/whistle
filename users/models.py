from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
# Create your models here.

class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    bio=models.TextField(blank=True,null=True)
    location=models.TextField(blank=True,null=True)
    phone_number=models.CharField(max_length=20,blank=True,null=True)
    profile_image=models.ImageField(upload_to='profile_image/',null=True,blank=True)
    cover_photo=models.ImageField(upload_to='cover_photo/',null=True,blank=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()
    def __str__(self):
        return self.email

