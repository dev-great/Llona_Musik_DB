from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name','artist', 'album_img', 'created', ]
    list_per_number = 50
    list_filter = ['artist', 'name', ]
    search_fields = ['name', 'artist',]


    def album_img(self, obj):
        return format_html('<img src="media/{}" style="width:30%; margin-left: 20%;" />'.format(obj.image))

    album_img.short_description = 'Image'


admin.site.register(Album, AlbumAdmin)

class MusicAdmin(admin.ModelAdmin):
    list_display = ['album', 'artist', 'ft', 'title','genre', 'note', ]
    list_per_number = 50
    list_filter = ['album', 'artist', 'ft', 'title','genre',]
    search_fields = ['album', 'artist', 'ft', 'title','genre',]

admin.site.register(MusicGallery, MusicAdmin)