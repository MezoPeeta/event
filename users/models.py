from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from io import BytesIO
from PIL import Image
import sys 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    bio = models.TextField(max_length=300)

    Committees = (
        ('IT','IT'),
        ('Design','Design'),
        ('PR','PR'),
        ('Logistics','Logistics'),
        ('HR','HR'),
        ('Marketing','Marketing'),
        ('Coaching','Coaching'),
        ('Media','Media'),
        ('Branding','Branding'),
    )
    committee = models.CharField(choices=Committees, max_length=10, default='')

    position_list = (
        ('Member', 'Member'),
        ('Head', 'Head'),
        ('Vice', 'Vice'),
        ('Co-President', 'Co-President'),
        ('President', 'President'),
    )
    position = models.CharField(choices=position_list, max_length=20, default='Member')

    awards = models.TextField(max_length=300, null= True)

    experience = models.TextField(max_length=300, null=True)

    achievement = models.TextField(max_length=300, null=True)
    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def get_absolute_url(self):
        return reverse('Profile', kwargs={'username': self.user.username})

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
  

        img = Image.open(self.image.path).convert('RGB')

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(f'{self.image.path}.jpg')
            

class RegistrationCode(models.Model):
    code = models.CharField(max_length=16)
    
    def __str__(self):
        return self.code

