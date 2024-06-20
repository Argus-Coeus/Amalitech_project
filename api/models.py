from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



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
    

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()