# Generated by Django 4.1.7 on 2023-03-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_profile_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Committee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name="profile",
            name="committee",
        ),
        migrations.AddField(
            model_name="profile",
            name="committee",
            field=models.ManyToManyField(blank=True, to="users.committee"),
        ),
    ]