from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from stories.models import Story,Comment
from stories.serializers import StorySerializer,CommentSerializer,CommentCreateSerializer,StoryCreateSerializer
from rest_framework.viewsets import ModelViewSet
from stories.permissions import IsAuthorOrReadOnly
# Create your views here.
@api_view()
def story_list(request):
    stories=Story.objects.all()
    serializer=StorySerializer(stories,many=True)
    return Response(serializer.data)

class StoryViewSet(ModelViewSet):
    serializer_class=StorySerializer
    queryset=Story.objects.prefetch_related('comments').all()
    permission_classes=[IsAuthorOrReadOnly]
    
    def get_queryset(self):
        author_id=self.request.query_params.get('user_id')
        if author_id is not None:
            return Story.objects.prefetch_related('comments').filter(author_id=author_id)
        return Story.objects.prefetch_related('comments').all()
    
    
    def get_serializer_class(self):
        if self.request.method in ['POST','PUT']:
            return StoryCreateSerializer
        return StorySerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    # auto update occured without perform_update() STRANGE

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


