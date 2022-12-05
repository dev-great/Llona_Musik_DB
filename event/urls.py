from django.urls import path
from .views import *

app_name = 'event'

urlpatterns = [
    path('events/', RetriveAllEventView.as_view()),
    path('events/<int:pk>/', RetriveEventViewByID.as_view()),
    path('tickets/', RetriveAllTicketView.as_view()),
    path('tickets/<int:pk>/', RetriveTicketViewByID.as_view()),
    path('pay/', PaymentView.as_view()),
]