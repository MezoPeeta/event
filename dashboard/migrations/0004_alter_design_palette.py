# Generated by Django 4.1.5 on 2023-02-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0003_design_generated_colors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="design",
            name="palette",
            field=models.ImageField(upload_to="palette"),
        ),
    ]