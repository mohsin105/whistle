from django.urls import path,include
from rest_framework_nested import routers
from stories.views import StoryViewSet,CommentViewSet,StoryImageViewSet
from users.views import initiate_payment, OrderViewSet, payment_success, payment_fail, payment_cancel
router=routers.DefaultRouter()

router.register('stories',StoryViewSet,basename='stories')
router.register('orders', OrderViewSet, basename='orders')

story_router=routers.NestedDefaultRouter(router,'stories',lookup='stories')
story_router.register('comments',CommentViewSet,basename='comments')
story_router.register('images',StoryImageViewSet,basename='story-images')

urlpatterns = [
    # path('stories/',include('stories.urls'))
    path('',include(router.urls)),
    path('',include(story_router.urls)),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('payment/initiate/', initiate_payment, name='initiate-payment'),
    path('payment/success/',payment_success, name='payment-success'),
    path('payment/cancel',payment_cancel, name='payment-cancel'),
    path('payment/fail/', payment_fail, name='payment-fail')
]

#personal story display er jonno another dedicated viewset create kore 
#separate router create kore shei router and path '/my-stories/' deya jay
