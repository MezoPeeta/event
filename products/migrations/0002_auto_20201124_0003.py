# Generated by Django 3.1.3 on 2020-11-23 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodcuts',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
