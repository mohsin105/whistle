from django.urls import path,include
from rest_framework_nested import routers
from stories.views import StoryViewSet,CommentViewSet,StoryImageViewSet
router=routers.DefaultRouter()
router.register('stories',StoryViewSet,basename='stories')

story_router=routers.NestedDefaultRouter(router,'stories',lookup='stories')
story_router.register('comments',CommentViewSet,basename='comments')
story_router.register('images',StoryImageViewSet,basename='story-images')

urlpatterns = [
    # path('stories/',include('stories.urls'))
    path('',include(router.urls)),
    path('',include(story_router.urls)),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt'))
]

#personal story display er jonno another dedicated viewset create kore 
#separate router create kore shei router and path '/my-stories/' deya jay
