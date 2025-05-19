from django.db import models
from users.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Story(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='stories')
    title=models.CharField(max_length=200,blank=True,null=True)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class StoryImage(models.Model):
    story=models.ForeignKey(Story,on_delete=models.CASCADE,related_name='images')
    image=CloudinaryField('image')
    # image=models.ImageField(upload_to='stories/images/')

    def __str__(self):
        return f'Image of {self.story.title}'
    
class Comment(models.Model):
    story=models.ForeignKey(Story,on_delete=models.CASCADE,related_name='comments')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'comment on {self.story.title} by {self.author.first_name}'

class Like(models.Model):
    story=models.ForeignKey(Story,on_delete=models.CASCADE,related_name='likes')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=['story','user']

    def __str__(self):
        return f'Like on {self.story.title} by {self.user.first_name}'