# Generated by Django 3.0.6 on 2020-06-03 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200604_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='committee',
            field=models.CharField(choices=[('IT', 'IT'), ('Design', 'Design'), ('ER', 'ER'), ('Design', 'Design'), ('Marketing', 'Marketing'), ('Coaching', 'Coaching'), ('Media', 'Media'), ('Branding', 'Branding')], max_length=10, null=True),
        ),
    ]
