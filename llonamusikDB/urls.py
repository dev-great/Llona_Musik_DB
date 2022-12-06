

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)


admin.site.site_header ="Llona control panel"
admin.site.index_title ="Administrators dashboard"
admin.site.site_title ="Control panel"