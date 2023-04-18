import base64
import uuid
from django.core.files.base import ContentFile
from apps.products.models import Products
from django.contrib.auth.models import User
from faker import Faker
import pygsheets
from django.shortcuts import redirect


def get_report_image(data):
    _, str_image = data.split(";base64")
    decoded_img = base64.b64decode(str_image)
    img_name = str(uuid.uuid4())[:10] + ".png"
    data = ContentFile(decoded_img, name=img_name)

    return data


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def generate_fake_products(num=10):
    fake = Faker()
    for _ in range(num):
        Products.objects.create(
            name=fake.name(),
            user=User.objects.get(pk=1),
            price=fake.random_int(min=1, max=100),
            image="products/default.png",
        )

    return "Done"


def google_sheet_auth():
    return pygsheets.authorize(client_secret="static/base/credentials.json")

def get_worksheet(sheet_url):
    gc = google_sheet_auth()
    try:
        sh = gc.open_by_url(sheet_url)
    except pygsheets.SpreadsheetNotFound:
        return "Give access permission to the sheet"
        
    
    wks = sh[0]

    return wks

def update_content(request,form,queryset: object):
    page,_ = queryset.objects.get_or_create(id=1)
    if request.method == "POST":
        form = form(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            page.title_en = form.cleaned_data["title_en"]
            page.title_ar = form.cleaned_data["title_ar"]
            page.content_en = form.cleaned_data["content_2_en"]
            page.content_ar = form.cleaned_data["content_ar"]
            page.save()

def update_2nd_content(request,form,queryset: object):
    page,_ = queryset.objects.get_or_create(id=1)
    if request.method == "POST":
        form = form(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            page.title_2_en = form.cleaned_data["title_2_en"]
            page.title_2_ar = form.cleaned_data["title_2_ar"]
            page.content_2_en = form.cleaned_data["content_2_en"]
            page.content_2_ar = form.cleaned_data["content_2_ar"]
            page.save()
