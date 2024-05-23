from rest_framework import serializers
from .models import Video
from django.contrib.auth.models import User
from .models import Video

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','title', 'description', 'Video_file', 'thumbnail', 'date_posted',)
        model = Video

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Video.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']