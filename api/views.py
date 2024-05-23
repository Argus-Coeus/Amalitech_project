from django.shortcuts import render
from rest_framework import generics
from .models import Video
from .serializers import PostSerializer,UserSerializer
from rest_framework import views
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from rest_framework.decorators import action



@action(detail=True, methods=['get'])
class PostList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = PostSerializer
    

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

