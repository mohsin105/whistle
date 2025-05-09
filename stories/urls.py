from django.urls import path
from stories.views import story_list
urlpatterns = [
    path('',story_list,name='news-feed')
]
