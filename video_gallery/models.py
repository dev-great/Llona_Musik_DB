from django.db import models
from event.models import Event
from tag.models import Tag
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class VideoGallery(models.Model):
    title = models.CharField(max_length=100, blank = False, null = False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    note = models.TextField(max_length=1000, blank = False, null = False)
    Video = CloudinaryField('video/', resource_type = "video", chunk_size = 5000000000,)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Video'
        verbose_name_plural = 'VideoGallery'

    def __str__(self):
        return self.title

