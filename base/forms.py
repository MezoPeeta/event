from django import forms
from .models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['id','name', 'email']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['id','name']
#hello 
