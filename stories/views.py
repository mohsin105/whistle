from django.shortcuts import render
from django.db.models import Count
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from stories.models import Story,Comment,StoryImage,Like
from stories.serializers import StorySerializer,CommentSerializer,CommentCreateSerializer,StoryCreateSerializer,StoryImageSerializer,StoryListSerializer
from rest_framework.viewsets import ModelViewSet
from stories.permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from stories.paginations import DefaultPagination
from stories.filters import StoryFilter
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
@api_view()
def story_list(request):
    stories=Story.objects.all()
    serializer=StorySerializer(stories,many=True)
    return Response(serializer.data)

class StoryViewSet(ModelViewSet):

    """
    Displays All Stories and their comments and images. 
    Any visitor can view stories. 
    Authenticated User can Create Story. 
    User can update his own story. 
    Admin can update any story. 
    """
    serializer_class=StorySerializer
    queryset=Story.objects.prefetch_related('comments').annotate(
        comment_count=Count('comments',distinct=True),
        like_count=Count('likes',distinct=True)
        ).all()
    permission_classes=[IsAuthorOrReadOnly]
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class=StoryFilter
    search_fields=['author__first_name','author__last_name','title']
    # filterset_fields=['author_id','author__first_name', 'author__last_name']
    pagination_class=DefaultPagination
    ordering_fields=['created_at','comment_count', 'like_count']
    # def get_queryset(self):
    #     author_id=self.request.query_params.get('user_id')
    #     if author_id is not None:
    #         return Story.objects.prefetch_related('comments').filter(author_id=author_id)
    #     return Story.objects.prefetch_related('comments').all()
    
    
    def get_serializer_class(self):
        if self.request.method in ['POST','PUT']:
            return StoryCreateSerializer
        if self.action=='list':
            return StoryListSerializer
        return StorySerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    # auto update occured without perform_update() STRANGE

    @action(detail=True,methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def like(self,request, pk=None):
        print('like action endpoind hit through action button')
        story=self.get_object()
        print(story.id)
        user=request.user
        print(user.first_name)
        if story.likes.filter(user_id=user.id).exists():
            #do unlike
            print('like ache already. unlike korte hobe')
            likeObj=story.likes.filter(user_id=user.id)
            likeObj.delete()
            return Response({'status':'Unlike Successfull'})
        else:
            #do like operation
            print('like nai. new like create korte hobe')
            Like.objects.create(story_id=story.id, user_id=user.id)
            return Response({'status':'Like Succesfull'})
    
    # wrong faulti code. crashes because of list view
    # def get_serializer_context(self):
    #     return {'is_liked': Like.objects.filter(story=self.get_object(),user=self.request.user).exists()}

    def list(self, request, *args, **kwargs):
        "Shows all stories with comment count and like count. "
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        "Shows a single story with all its comments and images"
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_summary='Create a single story',
            operation_description='An authenticated user can create a story',
            request_body=StoryCreateSerializer,
            responses={
                201:StorySerializer,
                401:'Bad Request'
            }
            )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_summary='Update a single story',
            operation_description='Allows normal user to update only his own story, admin can update any story',
            request_body=StoryCreateSerializer,
            responses={
                201:StorySerializer,
                403:'Bad Request'
            }
            )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_summary='Delete a single story',
            operation_description='Allows normal user to delete only his own story, admin can delete any story',
            request_body=StorySerializer,
            responses={
                204:'No Content',
                403:'Bad Request'
            }
            )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class StoryImageViewSet(ModelViewSet):
    serializer_class=StoryImageSerializer
    permission_classes=[IsAuthorOrReadOnly]

    def get_queryset(self):
        return StoryImage.objects.select_related('story').filter(story_id=self.kwargs.get('stories_id'))
    
    def perform_create(self, serializer):
        print('Story Id:::::::::::',self.kwargs.get('stories_pk'))
        serializer.save(story_id=self.kwargs.get('stories_pk'))

class CommentViewSet(ModelViewSet):
    permission_classes=[IsAuthorOrReadOnly]

    def get_queryset(self):
        
        if self.request.user.is_staff:
            return Comment.objects.filter(story_id=self.kwargs.get('stories_pk'))
        # return Comment.objects.all()
        return Comment.objects.filter(story_id=self.kwargs.get('stories_pk'))
    
    def get_serializer_class(self):
        if self.request.method in ['POST','PUT']:
            return CommentCreateSerializer
        return CommentSerializer
    
    def get_serializer_context(self):
        context={
            'user_id':self.request.user.id,
            'story_id':self.kwargs.get('stories_pk')
        }
        return context
    
    def perform_update(self, serializer):
        serializer.save(author_id=self.request.user.id,story_id=self.kwargs.get('stories_pk'))

    @swagger_auto_schema(
            operation_summary='Show all comment of the specific story',
            operation_description='Allows anyone to see all comments of the specific story',
            
            responses={
                200:CommentSerializer,
                401:'Bad Request'
            }
            )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

    @swagger_auto_schema(
            operation_summary='Create a single story',
            operation_description='An authenticated user can create a story',
            request_body=CommentCreateSerializer,
            responses={
                201:CommentSerializer,
                401:'Bad Request'
            }
            )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    

    @swagger_auto_schema(
            operation_summary='Shows a single comment of the specific story',
            operation_description='Allows anyone to see a single comments of the specific story',
            
            responses={
                201:StorySerializer,
                400:'Bad Request'
            }
            )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    

    @swagger_auto_schema(
            operation_summary='Update a single comment',
            operation_description='An authenticated user can update only his own comment',
            request_body=CommentCreateSerializer,
            responses={
                201:CommentSerializer,
                403:'Bad Request'
            }
            )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    

    @swagger_auto_schema(
            operation_summary='Delete a single comment',
            operation_description='An authenticated user can delete only his own comment',
            request_body=CommentSerializer,
            responses={
                204:'No Content',
                403:'Bad Request'
            }
            )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


'''Like feature View
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_like(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    like, created = Like.objects.get_or_create(user=request.user, story=story)

    if not created:
        like.delete()
        return Response({'message': 'Unliked'}, status=200)
    return Response({'message': 'Liked'}, status=201)
'''


