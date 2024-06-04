from rest_framework import serializers
from .models import Video
from django.contrib.auth.models import User
from .models import Video
from django.contrib.auth.tokens import default_token_generator






class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','title', 'description', 'Video_file', 'thumbnail', 'date_posted',)
        model = Video

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email','is_staff','is_active']

