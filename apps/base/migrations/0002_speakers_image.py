# Generated by Django 4.2 on 2023-05-04 19:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="speakers",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="speaker_pics"),
        ),
    ]
