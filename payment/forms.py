from django import forms
from .models import Ticket , TicketRecieved

class TicketForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    class Meta:
        model = Ticket
        fields = ['name', 'email']


class TicketRecievedForm(forms.ModelForm):
    class Meta:
        model = TicketRecieved
        fields = ['name','email','code']
    