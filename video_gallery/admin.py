from django.contrib import admin
from .models import *

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'event', 'note', 'created', ]
    list_per_number = 50
    list_filter = ['title', 'tag', 'event', ]
    search_fields = ['title', 'tag', 'event', ]


admin.site.register(VideoGallery, VideoAdmin)