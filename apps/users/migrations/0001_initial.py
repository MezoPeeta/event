# Generated by Django 4.1.7 on 2023-04-12 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Committee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("description", models.TextField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="RegistrationCode",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("phone", models.CharField(blank=True, max_length=20)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="profile_pics"),
                ),
                ("show_email", models.BooleanField(default=True)),
                ("show_phone", models.BooleanField(default=True)),
                ("bio", models.TextField(blank=True, max_length=300)),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("Member", "Member"),
                            ("Head", "Head"),
                            ("Vice", "Vice"),
                            ("Operations", "Operations"),
                            ("President", "President"),
                        ],
                        default="Member",
                        max_length=20,
                    ),
                ),
                ("awards", models.TextField(blank=True, max_length=300)),
                ("experience", models.TextField(blank=True, max_length=300)),
                ("achievement", models.TextField(blank=True, max_length=300)),
                ("facebook", models.CharField(blank=True, max_length=100)),
                ("instagram", models.CharField(blank=True, max_length=100)),
                ("twitter", models.CharField(blank=True, max_length=100)),
                ("linkedin", models.CharField(blank=True, max_length=100)),
                ("behance", models.CharField(blank=True, max_length=100)),
                ("dribbble", models.CharField(blank=True, max_length=100)),
                ("github", models.CharField(blank=True, max_length=100)),
                ("youtube", models.CharField(blank=True, max_length=100)),
                ("website", models.CharField(blank=True, max_length=100)),
                ("flickr", models.CharField(blank=True, max_length=100)),
                (
                    "committee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.committee",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "permissions": [
                    ("can_view_dashboard", "Can view dashboard"),
                    ("change_user_committee", "Can change user committee"),
                ],
            },
        ),
    ]
