from django import forms
from .models import ShippingAddress

class ShippingAddressClass(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address','phone_number','city' , 'state', 'zipcode']
