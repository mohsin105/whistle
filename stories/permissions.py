from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method=='POST':
            return request.user.is_authenticated
        return request.user and request.user.is_authenticated
        # return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if request.user.is_staff:
            return True
        
        if hasattr(obj,'author'):
            return obj.author == request.user
        else: #for image of the story
            return obj.story.author == request.user
        
        #hasattr(obj,'author')
        # return super().has_object_permission(request, view, obj)