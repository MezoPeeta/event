# Generated by Django 3.2.1 on 2021-05-12 21:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20201130_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
