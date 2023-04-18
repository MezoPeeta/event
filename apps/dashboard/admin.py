from django.contrib import admin
from .models import Report, HomePage, AboutPage
from modeltranslation.admin import TranslationAdmin

admin.site.register(Report)

class PageAdmin(TranslationAdmin):
    pass

admin.site.register(HomePage, PageAdmin)
admin.site.register(AboutPage, PageAdmin)


