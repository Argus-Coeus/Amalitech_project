# Generated by Django 5.0.6 on 2024-05-27 12:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_uploader_video_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='Video_file',
            field=models.FileField(upload_to='media/uploads/video_files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.FileField(upload_to='media/uploads/thumbnails', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])]),
        ),
    ]
