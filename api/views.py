from django.shortcuts import render
from rest_framework import generics
from .models import Video
from .serializers import PostSerializer,UserSerializer
from rest_framework import views
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.views import LoginView,RedirectURLMixin
from django.shortcuts import redirect

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'create': reverse('create', request=request, format=format),
        'users': reverse('users-list', request=request, format=format),
        'Listing': reverse('listing', request=request, format=format)
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


class Login(LoginView,RedirectURLMixin):
    redirect_authenticated_user = True
    redirect_field_name = ''
    template_name = 'rest_framework/templates/login.html'

