

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('event.urls', namespace='event')),
    path('musics/', include('music_gallery.urls', namespace='music_gallery')),
    path('videos/', include('video_gallery.urls', namespace='video_gallery')),
    path('photos/', include('photo_gallery.urls', namespace='photo_gallery')),
]

