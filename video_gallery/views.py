from .models import *
from .serializer import *
from tag.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
# Create your views here.

class RetriveAllVideosView(APIView):

    def get(self, request):
        video_file = VideoGallery.objects.all()
        serializer = VideoSerializer(video_file, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetriveEventVideosView(APIView):



    def get(self, request, tag):
        qs = tag.capitalize()
        tag_qs = Tag.objects.get(name=qs)
        if VideoGallery.objects.filter(tag=tag_qs).exists():
            tag_qs = VideoGallery.objects.filter(tag=tag_qs)
            serializer = VideoSerializer(tag_qs, many=True)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Report": "No Match found"}, status=status.HTTP_400_BAD_REQUEST)



class RetriveVideosByIDView(APIView):

    def get(self, request, pk):
        if VideoGallery.objects.filter(pk__exact=pk).exists():
            pk_qs = VideoGallery.objects.get(pk__exact=pk)
            serializer = VideoSerializer(pk_qs)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Report": "No Match found"}, status=status.HTTP_400_BAD_REQUEST)
