from django.urls import path
from .views import *

app_name = 'music_gallery'

urlpatterns = [
    path('album/', RetriveAllAlbumView.as_view()),
    path('music/', RetriveAllMusicView.as_view()),
    path('genre/<str:genre>/', RetriveGenreMusicView.as_view()),
    path('album/<str:album>/', RetriveMusicViewByAlbum.as_view()),
    path('artist/<str:artist>/', RetriveMusicViewByArtist.as_view()),
    path('music/<int:pk>/', RetriveMusicViewByID.as_view()),
]