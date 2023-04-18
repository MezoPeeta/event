from apps.base.models import Contact
from django import forms
from .models import Report, HomePage, AboutPage
from ckeditor.fields import RichTextFormField


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["name", "remarks"]


class ContactForm(forms.ModelForm):
    reply = RichTextFormField()

    class Meta:
        model = Contact
        fields = ["reply"]


class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = ['title_en','content_en','title_ar','content_ar']

class HomeSecondPageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = ['title_2_en','content_2_en','title_2_ar','content_2_ar']


class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ['title_en','content_en','title_ar','content_ar']

class AboutSecondPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ['title_2_en','content_2_en','title_2_ar','content_2_ar']
