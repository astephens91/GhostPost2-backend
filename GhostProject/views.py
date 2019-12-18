from rest_framework import viewsets

from GhostProject.models import Post
from GhostProject.serializers import PostSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
