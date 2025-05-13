from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from stories.models import Story,Comment
from stories.serializers import StorySerializer,CommentSerializer,CommentCreateSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
@api_view()
def story_list(request):
    stories=Story.objects.all()
    serializer=StorySerializer(stories,many=True)
    return Response(serializer.data)

class StoryViewSet(ModelViewSet):
    serializer_class=StorySerializer
    queryset=Story.objects.prefetch_related('comments').all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    # auto update occured without perform_update() STRANGE

class CommentViewSet(ModelViewSet):


    def get_queryset(self):
        if self.request.user.is_staff:
            return Comment.objects.filter(story_id=self.kwargs.get('stories_pk'))
        return Comment.objects.all()
    
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


