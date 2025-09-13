from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from cloudinary.models import CloudinaryField
from uuid import uuid4
# Create your models here.

class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    bio=models.TextField(blank=True,null=True)
    location=models.TextField(blank=True,null=True)
    phone_number=models.CharField(max_length=20,blank=True,null=True)
    profile_image=CloudinaryField('image',null=True,blank=True)
    # profile_image=models.ImageField(upload_to='profile_image/',null=True,blank=True)
    cover_photo=CloudinaryField('image',null=True,blank=True)
    # cover_photo=models.ImageField(upload_to='cover_photo/',null=True,blank=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()
    def __str__(self):
        return self.email


class Order(models.Model):
    ORDER_STATUS=[
        ('PENDING','Pending'),
        ('ACTIVE','Active'),
        ('PAUSED','Paused')
    ]
    id=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    package_name=models.CharField(max_length=100)
    status=models.CharField(max_length=20, choices=ORDER_STATUS, default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    price=models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f'{self.id} by {self.user.first_name}'