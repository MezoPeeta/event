from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Videos(models.Model):
    id = models.AutoField(primary_key=True)
    urlID = models.CharField(max_length=300,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=500, default='video')
    date_posted= models.DateTimeField(default=timezone.now)     

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('WatchUs')

class Subscribe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12)
    email = models.EmailField()
    subscribed = models.BooleanField(default=False)
    date_subscribed= models.DateTimeField(default=timezone.now)     

    def __str__(self):
        return f'{self.name}'



class Contact(models.Model):
    id = models.AutoField(primary_key=True)#
    name = models.CharField(max_length=12)
    email = models.EmailField()
    subject = models.CharField(max_length=12)
    message = models.TextField()
    reply = RichTextField(null=True,blank=True)#
    created= models.DateTimeField(default=timezone.now)  #   
    
    def __str__(self):
        return f'{self.name}'

class Speakers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg',upload_to='speaker_pics')
    talk_name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)  
    youtube = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    date_posted= models.DateTimeField(default=timezone.now)   

class ImageSpeakers(models.Model):
    name = models.CharField(max_length=255)
    speaker = models.ForeignKey(Speakers, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='speaker_pics')
    default = models.BooleanField(default=False) 
