# Generated by Django 4.1.3 on 2022-12-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_alter_profile_committee_alter_profile_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='committee',
            field=models.CharField(blank=True, choices=[('IT', 'IT'), ('Design', 'Design'), ('PR', 'PR'), ('Logistics', 'Logistics'), ('HR', 'HR'), ('Marketing', 'Marketing'), ('Coaching', 'Coaching'), ('Media', 'Media')], max_length=10, null=True),
        ),
    ]
