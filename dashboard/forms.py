from base.models import Contact
from django import forms
from .models import Report , Design
from ckeditor.fields import RichTextFormField

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'remarks']

class ContactForm(forms.ModelForm):
    reply = RichTextFormField()
    class Meta:
        model = Contact
        fields = ['reply']

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = ['color']