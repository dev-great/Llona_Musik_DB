from rest_framework import serializers
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicGallery
        fields = '__all__'