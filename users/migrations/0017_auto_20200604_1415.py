# Generated by Django 3.0.6 on 2020-06-04 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20200604_0037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='skills',
            new_name='achievement',
        ),
    ]
