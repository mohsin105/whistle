from rest_framework import serializers
from stories.models import Story,StoryImage,Comment
from users.serializers import SimpleUserViewSerializer

class CommentSerializer(serializers.ModelSerializer):
    author=SimpleUserViewSerializer()
    class Meta:
        model=Comment
        fields=['id','author','story','content']

class StoryImageSerializer(serializers.ModelSerializer):
    image=serializers.ImageField()
    
    class Meta:
        model=StoryImage
        fields=['id','image'] 

class StorySerializer(serializers.ModelSerializer):
    author=SimpleUserViewSerializer()
    images=StoryImageSerializer(many=True)
    comments=CommentSerializer(many=True)
    like_count=serializers.IntegerField()
    
    class Meta:
        model=Story
        fields=['id','author','title','content','images','comments', 'like_count']
        read_only_fields=['author']

class StoryListSerializer(serializers.ModelSerializer):
    comment_count=serializers.IntegerField(help_text='Shows the number of comments in this story')
    like_count=serializers.IntegerField(help_text='Shows the number of Likes in this story')
    # author=serializers.StringRelatedField()
    
    author=SimpleUserViewSerializer()
    images=StoryImageSerializer(many=True)
    
    class Meta:
        model=Story
        fields=['id','author','title','content','comment_count','like_count','images']

class StoryCreateSerializer(serializers.ModelSerializer):
    # images=StoryImageSerializer()

    class Meta:
        model=Story
        fields=['id','title','content']



class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','content']
    
    def create(self, validated_data):
        story_id=self.context['story_id']
        user_id=self.context['user_id']
        comment=Comment.objects.create(author_id=user_id,story_id=story_id,**validated_data)
        return comment