from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'theater', 'city', 'state', 'start_time', 'end_time', 'event_img','available_seats','created', ]
    list_per_number = 50
    list_filter = ['name', 'theater', 'city', 'state',]
    search_fields = ['name', 'theater', 'city', 'state',]


    def event_img(self, obj):
        return format_html('<img src="media/{}" style="width:30%; margin-left: 20%;"/>'.format(obj.image))

    event_img.short_description = 'Image'

admin.site.register(Event, EventAdmin)

class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'ticket', 'number_tickets', 'total_seats', 'active','created',]
    list_per_number = 50
    list_filter = ['event', 'ticket', 'active',]
    search_fields = ['event','ticket', 'active',]

admin.site.register(Ticket, TicketAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'ticket', 'on_tickets', 'last_name', 'first_name','email','paid','tranx_code','date_created', ]
    list_per_number = 50
    list_filter = ['ticket', 'tranx_code', 'paid', 'date_created',]
    search_fields = ['ticket','last_name', 'tranx_code', 'email', 'first_name',]


admin.site.register(Payment, PaymentAdmin)
