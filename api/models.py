from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class Video(models.Model):
    author   = models.ForeignKey(User,on_delete=models.CASCADE)
    right   = User.is_staff
    title = models.CharField(max_length=100)
    description = models.TextField()
    Video_file = models.FileField(upload_to='uploads/video_files',validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail = models.FileField(upload_to='uploads/thumbnails',validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'])])
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title