from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(max_length=300,blank=True)

    Committees = (
        ("IT", "IT"),
        ("Design", "Design"),
        ("PR", "PR"),
        ("Logistics", "Logistics"),
        ("HR", "HR"),
        ("Marketing", "Marketing"),
        ("Coaching", "Coaching"),
        ("Media", "Media"),
    )
    committee = models.CharField(
        choices=Committees, max_length=10, null=True, blank=True
    )

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

    image = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def get_absolute_url(self):
        return reverse("Profile", kwargs={"username": self.user.username})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path).convert("RGB")

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(f"{self.image.path}.jpg")


class RegistrationCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=16)

    def __str__(self):
        return self.code
