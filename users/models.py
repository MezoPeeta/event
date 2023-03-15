from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Committee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)

    bio = models.TextField(max_length=300, blank=True)

    committee = models.ManyToManyField(Committee, blank=True)

    position_list = (
        ("Member", "Member"),
        ("Head", "Head"),
        ("Vice", "Vice"),
        ("Operations", "Operations"),
        ("President", "President"),
    )
    position = models.CharField(choices=position_list, max_length=20, default="Member")

    awards = models.TextField(max_length=300, blank=True)

    experience = models.TextField(max_length=300, blank=True)

    achievement = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def get_absolute_url(self):
        return reverse("Profile", kwargs={"username": self.user.username})

    def save(self, *args, **kwargs):
        if self.image:
            super().save(*args, **kwargs)
            img = Image.open(self.image.path).convert("RGB")

            if img.height > 300 or img.width > 300:
                new_img = (300, 300)
                img.thumbnail(new_img)
                img.save(f"{self.image.path}.jpg")
        else:
            super().save(*args, **kwargs)


class RegistrationCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=16)

    def __str__(self):
        return self.code
