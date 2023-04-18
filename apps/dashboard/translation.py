from modeltranslation.translator import translator, TranslationOptions
from .models import HomePage, AboutPage


class PageTranslationOptions(TranslationOptions):
    fields = ("title", "content", "title_2", "content_2")

    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


translator.register(HomePage, PageTranslationOptions)
translator.register(AboutPage, PageTranslationOptions)
