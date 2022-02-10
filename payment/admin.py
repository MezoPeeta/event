from django.contrib import admin
from .models import TicketForm, QrCode , Ticket_Recieved

class TicketModel(admin.ModelAdmin):
    list_display = ('id',"name" , 'email')
admin.site.register(TicketForm, TicketModel)

class TicketModel(admin.ModelAdmin):
    list_display = ("name" , 'email')
admin.site.register(Ticket_Recieved, TicketModel)

admin.site.register(QrCode)