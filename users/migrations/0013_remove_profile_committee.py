# Generated by Django 3.0.6 on 2020-06-03 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200604_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='committee',
        ),
    ]
