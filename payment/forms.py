from django import forms
from .models import TicketForm , Ticket_Recieved

class Ticket_Form(forms.ModelForm):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    class Meta:
        model = TicketForm
        fields = ['name', 'email']


class TicketRecieved(forms.ModelForm):
    class Meta:
        model = Ticket_Recieved
        fields = ['name','email','code']
    