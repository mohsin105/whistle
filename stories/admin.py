from django.contrib import admin
from stories.models import Story,StoryImage,Comment,Like
# Register your models here.

admin.site.register(Story)
admin.site.register(Comment)
admin.site.register(Like)
