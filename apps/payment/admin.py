from django.contrib import admin
from .models import Ticket, QrCode , TicketRecieved

class TicketModel(admin.ModelAdmin):
    list_display = ('id',"name" , 'email')
    
admin.site.register(Ticket, TicketModel)

admin.site.register(TicketRecieved, TicketModel)

admin.site.register(QrCode)