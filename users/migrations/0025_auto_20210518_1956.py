# Generated by Django 3.2.1 on 2021-05-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_registrationcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='committee',
            field=models.CharField(choices=[('IT', 'IT'), ('Design', 'Design'), ('PR', 'PR'), ('Logistics', 'Logistics'), ('HR', 'HR'), ('Marketing', 'Marketing'), ('Coaching', 'Coaching'), ('Media', 'Media'), ('Branding', 'Branding')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Member', 'Member'), ('Head', 'Head'), ('Vice', 'Vice'), ('Co-President', 'Co-President'), ('President', 'President')], default='Member', max_length=20),
        ),
    ]
