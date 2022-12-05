from django.shortcuts import render

# Create your views here.
from .models import *
from event.models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
# Create your views here.

class RetriveAllImagesView(APIView):
    
    def get(self, request):
        image_file = PhotoGallery.objects.all()
        serializer = PhotoSerializer(image_file, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetriveEventImagesView(APIView):

    def get(self, request, tag):
        qs = tag.capitalize()
        tag_qs = Tag.objects.get(name=qs)
        if PhotoGallery.objects.filter(tag=tag_qs).exists():
            tag_qs = PhotoGallery.objects.filter(tag=tag_qs)
            serializer = PhotoSerializer(tag_qs, many=True)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Report": "No Match found"}, status=status.HTTP_400_BAD_REQUEST)

class RetriveImagesViewByID(APIView):

    def get(self, request, pk):
        if PhotoGallery.objects.filter(pk__exact=pk).exists():
            pk_qs = PhotoGallery.objects.get(pk__exact=pk)
            serializer = PhotoSerializer(pk_qs)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Report": "No Match found"}, status=status.HTTP_400_BAD_REQUEST)
