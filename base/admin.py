from django.contrib import admin
from .models import Contact, Videos, Subscribe, Speakers

admin.site.site_header = "TEDx ManaratAlFarouk School"
admin.site.site_title = "TEDx ManaratAlFarouk School"


class VideosModel(admin.ModelAdmin):
    fields = ("urlID", "name")
    list_display = ("name", "date_posted", "user")


admin.site.register(Videos, VideosModel)


class SubscribeModel(admin.ModelAdmin):
    list_display = ("name", "email", "subscribed", "date_subscribed")


admin.site.register(Subscribe, SubscribeModel)


class ContactModel(admin.ModelAdmin):
    list_display = ("name", "subject", "email")


admin.site.register(Contact, ContactModel)


class SpeakersModel(admin.ModelAdmin):
    list_display = ("name", "talk_name")


admin.site.register(Speakers, SpeakersModel)
