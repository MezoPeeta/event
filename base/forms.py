from django import forms
from .models import Subscribe

class Subscribe_Form(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['id','name', 'email']

class Newsletter_Form(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['id','name']

