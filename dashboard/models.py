from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from colorfield.fields import ColorField

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120,null=True)
    image = models.ImageField(upload_to='reports',blank=True)
    remarks = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('Reports_Detail',kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.name)

class Design(models.Model):
    id = models.AutoField(primary_key=True)
    color = ColorField(default='#ff2a2a')
    font_color = ColorField(default='#ffffff')
    palette = models.ImageField(upload_to='palette',null=True)
    generated_colors = models.TextField(blank=True)

    def __str__(self):
        return str(self.color)