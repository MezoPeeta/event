# Generated by Django 4.1.7 on 2023-03-23 18:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_profile_dribbble_profile_github"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="website",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
