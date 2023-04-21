from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Committee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    ip_address = models.CharField(max_length=50, blank=True)
    image = models.ImageField(
        upload_to="profile_pics",
        blank=True,
        null=True,
    )
    show_email = models.BooleanField(default=True)
    show_phone = models.BooleanField(default=True)
    bio = models.TextField(max_length=300, blank=True)

    committee = models.ForeignKey(
        Committee, on_delete=models.CASCADE, blank=True, null=True
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

    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    behance = models.CharField(max_length=100, blank=True)
    dribbble = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    youtube = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    flickr = models.CharField(max_length=100, blank=True)

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
    
    class Meta:
        permissions = [
            ("can_view_dashboard", "Can view dashboard"),
            ("change_user_committee", "Can change user committee"),
            
        ]


class RegistrationCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=16)

    def __str__(self):
        return self.code
