from django.shortcuts import render

# Create your views here.
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
# Create your views here.

class RetriveAllEventView(APIView):
    
    def get(self, request):
        event_qs = Event.objects.all()
        serializer = EventSerializer(event_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetriveEventViewByID(APIView):

    def get(self, request, pk):
        pk_qs = Event.objects.get(pk__exact=pk)
        if Event.objects.filter(pk__exact=pk).exists():
            pk_qs = Event.objects.get(pk__exact=pk)
            serializer = EventSerializer(pk_qs)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Report": "No Match found"}, status=status.HTTP_400_BAD_REQUEST)


class RetriveAllTicketView(APIView):
    
    def get(self, request):
        ticket_qs = Ticket.objects.all()
        serializer = TicketSerializer(ticket_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetriveTicketViewByID(APIView):

    def get(self, request, pk):
        if Ticket.objects.filter(pk__exact=pk).exists():
            pk_qs = Ticket.objects.get(pk__exact=pk)
            serializer = TicketSerializer(pk_qs)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Report": "No Match found"}, status=status.HTTP_400_BAD_REQUEST)


class PaymentView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({"Report": "There was a problem processing your payment"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)