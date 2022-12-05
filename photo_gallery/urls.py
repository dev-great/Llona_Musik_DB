from django.urls import path
from .views import *

app_name = 'photo_gallery'

urlpatterns = [
    path('', RetriveAllImagesView.as_view()),
    path('tag/<str:tag>/', RetriveEventImagesView.as_view()),
    path('<int:pk>/', RetriveImagesViewByID.as_view()),
]