from apps.base.models import Contact
from django import forms
from .models import Report
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
