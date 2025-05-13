from rest_framework import serializers
from stories.models import Story,StoryImage,Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','author','story','content']
    
class StorySerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True)
    class Meta:
        model=Story
        fields=['id','author','title','content','comments']
        read_only_fields=['author']


class StoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=StoryImage
        fields=['id','image']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','content']
    
    def create(self, validated_data):
        story_id=self.context['story_id']
        user_id=self.context['user_id']
        comment=Comment.objects.create(author_id=user_id,story_id=story_id,**validated_data)
        return comment