from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField


class Album(models.Model):
    name = models.CharField(max_length=300)
    image = CloudinaryField('image')
    artist = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.name

class MusicGallery(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    artist = models.CharField(max_length=100)
    ft = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=100, blank = False, null = False)
    genre = models.CharField(max_length=100, blank = False, null = False)
    note = models.TextField(max_length=1000, blank = False, null = False)
    music = CloudinaryField(resource_type='raw')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created',)
        verbose_name = 'Music'
        verbose_name_plural = 'Musics'

    def __str__(self):
        return self.title
