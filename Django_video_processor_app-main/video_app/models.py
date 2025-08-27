from django.db import models
class VideoUpload(models.Model):
    video = models.FileField(upload_to='videos/')
    subtitle = models.FileField(upload_to='subtitles/', blank=True, null=True)
    title = models.CharField(max_length=255)
    def __str__(self):
            return self.title

