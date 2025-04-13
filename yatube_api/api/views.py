from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAuthor
from rest_framework.decorators import permission_classes

from posts.models import Post, Group, Comment, Follow
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer


@permission_classes([IsAuthenticatedOrReadOnly, IsAuthor])
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@permission_classes([IsAuthenticatedOrReadOnly])
class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@permission_classes([IsAuthenticatedOrReadOnly, IsAuthor])
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


@permission_classes([IsAuthenticated, IsAuthor])
class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)