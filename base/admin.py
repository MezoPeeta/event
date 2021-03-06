from dashboard.forms import ContactForm
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact, Videos , Subscribe

admin.site.site_header = "TEDx ManaratAlFarouk School"
admin.site.site_title = "TEDx ManaratAlFarouk School"


class VideosModel(admin.ModelAdmin):
    fields = ('urlID' , 'name')
    list_display = ('name' , 'date_posted', 'memberName')

admin.site.register(Videos, VideosModel)

class SubscribeModel(admin.ModelAdmin):
    list_display = ('name' , 'email','subscribed','date_subscribed')


admin.site.register(Subscribe, SubscribeModel)



class ContactModel(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email')

admin.site.register(Contact,ContactModel)

