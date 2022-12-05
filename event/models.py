from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.timezone import now
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your models here.

Ticket_Type = (
        ('Regular','Regular'),
        ('Bronze', 'Bronze'),
        ('Gold', 'Gold'),
        ('platinum', 'platinum'),
        ('Black', 'Black'),
        ('Vip', 'Vip'),
    )

class Event(models.Model):
    name = models.CharField(max_length=1000)
    image = CloudinaryField('image')
    theater = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    location = models.CharField(max_length=1000)
    detailes = models.TextField(max_length=3000)
    start_time = models.DateTimeField(auto_now_add=True, blank=False)
    end_time = models.DateTimeField(auto_now_add=True, blank=False)
    available_seats = models.IntegerField(default=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='Ticket_Type')
    image = CloudinaryField('image')
    price = models.IntegerField()
    ticket = models.CharField(max_length=20, choices=Ticket_Type)
    total_seats = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    number_tickets = models.IntegerField()
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.ticket


class Payment(models.Model): 
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING)
    on_tickets = models.IntegerField()
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=500)
    tranx_code = models.CharField(max_length=200)
    paid = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

@ receiver(post_save, sender=Payment)
def generate_ticket_record(sender, instance, *args, **kwargs):
    if instance:

       reduce_ticket = Ticket.objects.get(ticket=instance.ticket)
       if reduce_ticket.total_seats != 0 or reduce_ticket.total_seats != 0:
        reduce_ticket.number_tickets =  reduce_ticket.number_tickets - instance.on_tickets
        reduce_ticket.total_seats = reduce_ticket.total_seats - instance.on_tickets
        return reduce_ticket.save()

    #    merge_data = {
    #     'lendeet_user':  f"{loged_in_user.email}", 
    #     'msg': f" Hi {loged_in_user.first_name} {loged_in_user.last_name} Your withdrawal of {instance.amount} has been placed sucessfully."
    #     }
    #    html_body = render_to_string("emails/congratulation_mail.html", merge_data)
    #    msg = EmailMultiAlternatives(subject="Withdwal of funds", from_email=settings.EMAIL_HOST_USER, to=[user_email], body=" ",)
    #    msg.attach_alternative(html_body, "text/html")
    #    return msg.send(fail_silently=False)
