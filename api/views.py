from django.shortcuts import render
from rest_framework import generics
from .models import Video
from .serializers import PostSerializer,UserSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_rest_passwordreset.views import ResetPasswordConfirm
from django_rest_passwordreset.serializers import PasswordTokenSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_root(request, format=None):
    return Response({
        'Create a video ': reverse('create', request=request, format=format),
        'Listing video Upload': reverse('listing', request=request, format=format),
        'Listing users': reverse('users-list', request=request, format=format),
        'Token Generator': reverse('token_obtain_pair', request=request, format=format),
        'Token Refresh': reverse('token_refresh', request=request, format=format),
        'Account Register': reverse('auth_register', request=request, format=format),
        'Account LOgout': reverse('auth_logout', request=request, format=format),

    })

class CreateList(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class PostList(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class CustomResetPasswordConfirmView(ResetPasswordConfirm):
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PasswordTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Password has been reset with the new password.'}, status=status.HTTP_200_OK)
