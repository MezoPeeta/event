# Generated by Django 4.1.7 on 2023-04-10 23:24

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=12)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=12)),
                ("message", models.TextField()),
                ("reply", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Speakers",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("talk_name", models.CharField(max_length=20)),
                ("description", models.TextField(blank=True)),
                ("facebook", models.CharField(blank=True, max_length=100)),
                ("instagram", models.CharField(blank=True, max_length=100)),
                ("twitter", models.CharField(blank=True, max_length=100)),
                ("youtube", models.CharField(blank=True, max_length=100)),
                ("website", models.CharField(blank=True, max_length=100)),
                (
                    "date_posted",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subscribe",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=12)),
                ("email", models.EmailField(max_length=254)),
                ("subscribed", models.BooleanField(default=False)),
                (
                    "date_subscribed",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Videos",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("urlID", models.CharField(max_length=300, null=True)),
                ("name", models.CharField(default="video", max_length=500)),
                (
                    "date_posted",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ImageSpeakers",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(default="default.jpg", upload_to="speaker_pics"),
                ),
                ("default", models.BooleanField(default=False)),
                (
                    "speaker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.speakers"
                    ),
                ),
            ],
        ),
    ]
