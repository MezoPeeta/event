# Generated by Django 3.0.6 on 2020-06-03 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200604_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Member', 'Member'), ('Head', 'Head'), ('Vice', 'Vice'), ('President', 'President')], default='Member', max_length=10),
        ),
    ]
