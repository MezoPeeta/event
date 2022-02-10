from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Report(models.Model):
    name = models.CharField(max_length=120,null=True)
    image = models.ImageField(upload_to='reports',blank=True)
    remarks = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('Reports_Detail',kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.name)
