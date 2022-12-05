from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
# Create your views here.

class RetriveAllAlbumView(APIView):
    
    def get(self, request):
        album_qs = Album.objects.all()
        serializer = AlbumSerializer(album_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetriveAllMusicView(APIView):
    
    def get(self, request):
        music_file = MusicGallery.objects.all()
        serializer = MusicSerializer(music_file, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetriveGenreMusicView(APIView):


    def get(self, request, genre):
        qs = genre.capitalize()
        if MusicGallery.objects.filter(genre=qs).exists():
            genre_qs = MusicGallery.objects.filter(genre=qs)
            serializer = MusicSerializer(genre_qs, many=True)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Report": "No Match found"}, status=status.HTTP_400_BAD_REQUEST)


class RetriveMusicViewByAlbum(APIView):


    def get(self, request, album):
        qs = album.capitalize()
        album_qs = Album.objects.get(name = qs)
        if MusicGallery.objects.filter(album=album_qs).exists():
            music_qs = MusicGallery.objects.filter(album=album_qs)
            serializer = MusicSerializer(music_qs, many=True)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Report": "No Match found"}, status=status.HTTP_400_BAD_REQUEST)


class RetriveMusicViewByArtist(APIView):

    def get(self, request, artist):
        qs = artist.capitalize()
        if MusicGallery.objects.filter(artist=qs).exists():
            artist_qs = MusicGallery.objects.filter(artist=artist)
            serializer = MusicSerializer(artist_qs, many=True)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Report": "No Match found"}, status=status.HTTP_400_BAD_REQUEST)

class RetriveMusicViewByID(APIView):

    def get(self, request, pk):
        if MusicGallery.objects.filter(pk__exact=pk).exists():
            pk_qs = MusicGallery.objects.get(pk__exact=pk)
            serializer = MusicSerializer(pk_qs)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Report": "No Match found"}, status=status.HTTP_400_BAD_REQUEST)
