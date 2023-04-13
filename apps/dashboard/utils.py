import base64
import uuid
from django.core.files.base import ContentFile
from apps.products.models import Products
from django.contrib.auth.models import User
from faker import Faker
import pandas as pd
import pygsheets


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


def sync_excel():
    gc = pygsheets.authorize(service_file="static/base/credentials.json")
    sheet = gc.open_by_url(
        "https://docs.google.com/spreadsheets/d/1YIlY7V6wpyEW-L33apgdXSuLQ0pcDOjnruVnRGVLVPE/edit#gid=0"
    )
    wks = sheet[0]
    data = wks.get_all_values(returnas="dataframe")
    print(data)

