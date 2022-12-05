from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'event', 'note','image_tag','created', ]
    list_per_number = 50
    list_filter = ['title', 'tag', 'event',]
    search_fields = ['title', 'tag', 'event',]

    def image_tag(self, obj):
        return format_html('<img src="/media/{}" style="width:30%; margin-left: 20%;" />'.format(obj.image))

    image_tag.short_description = 'Image'


admin.site.register(PhotoGallery, PhotoAdmin)