# Generated by Django 4.2 on 2023-04-14 13:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_products_google_sheet"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="products",
            name="google_sheet",
        ),
    ]