# Generated by Django 4.1.3 on 2022-12-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_alter_ticket_recieved_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ticket_recieved',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ticketform',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
