# Generated by Django 4.1.5 on 2023-02-01 00:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_design_palette"),
    ]

    operations = [
        migrations.AddField(
            model_name="design",
            name="generated_colors",
            field=models.TextField(blank=True),
        ),
    ]