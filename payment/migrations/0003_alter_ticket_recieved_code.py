# Generated by Django 3.2.1 on 2021-05-18 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20210518_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_recieved',
            name='code',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.qrcode'),
        ),
    ]
