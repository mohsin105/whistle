from django.urls import path,include
from rest_framework_nested import routers
from stories.views import StoryViewSet,CommentViewSet
router=routers.DefaultRouter()
router.register('stories',StoryViewSet,basename='stories')

story_router=routers.NestedDefaultRouter(router,'stories',lookup='stories')
story_router.register('comments',CommentViewSet,basename='comments')
urlpatterns = [
    # path('stories/',include('stories.urls'))
    path('',include(router.urls)),
    path('',include(story_router.urls))
]
