# Generated by Django 4.1.3 on 2023-01-14 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_products_name_products_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='product_default.jpg', null=True, upload_to='products'),
        ),
    ]
