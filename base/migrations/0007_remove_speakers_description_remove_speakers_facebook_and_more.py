# Generated by Django 4.1.7 on 2023-04-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0006_speakers_facebook_speakers_instagram_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="speakers",
            name="description",
        ),
        migrations.RemoveField(
            model_name="speakers",
            name="facebook",
        ),
        migrations.RemoveField(
            model_name="speakers",
            name="instagram",
        ),
        migrations.RemoveField(
            model_name="speakers",
            name="twitter",
        ),
        migrations.RemoveField(
            model_name="speakers",
            name="website",
        ),
        migrations.RemoveField(
            model_name="speakers",
            name="youtube",
        ),
        migrations.AddField(
            model_name="speakers",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="speakers_pics"),
        ),
        migrations.AlterField(
            model_name="speakers",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.DeleteModel(
            name="ImageSpeakers",
        ),
    ]
