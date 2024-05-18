from rest_framework import serializers
from .models import Video


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','title', 'description', 'Video_file', 'thumbnail', 'date_posted',)
        model = Video