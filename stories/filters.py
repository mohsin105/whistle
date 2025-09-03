from django_filters.rest_framework import FilterSet
from stories.models import Story

class StoryFilter(FilterSet):
    class Meta:
        model=Story
        fields={
            'author__first_name':['icontains'],
            'author__last_name': ['icontains']
        }