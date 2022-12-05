from django.urls import path
from .views import *

app_name = 'video_gallery'

urlpatterns = [
    path('', RetriveAllVideosView.as_view()),
    path('tag/<str:tag>/', RetriveEventVideosView.as_view()),
    path('<int:pk>/', RetriveVideosByIDView.as_view()),
]