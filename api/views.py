from django.shortcuts import render
from rest_framework import generics
from .models import Video
from .serializers import PostSerializer,UserSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Create a video ': reverse('create', request=request, format=format),
        'Listing video Upload': reverse('listing', request=request, format=format),
        'Listing users': reverse('users-list', request=request, format=format),
        'Token Generator': reverse('token_obtain_pair', request=request, format=format),
        'Token Refresh': reverse('token_refresh', request=request, format=format),
        'Account Register': reverse('auth_register', request=request, format=format),

    })

class CreateList(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

class PostList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
