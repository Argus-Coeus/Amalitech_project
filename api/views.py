from django.shortcuts import render
from rest_framework import generics
from .models import Video
from .serializers import PostSerializer
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = PostSerializer
