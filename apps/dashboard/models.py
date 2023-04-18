from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

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

class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120,null=True)
    title_2 = models.CharField(max_length=120,null=True)
    content = models.TextField()
    content_2 = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class HomePage(Page):
    def __str__(self):
        return str(self.title)

class AboutPage(Page):
    def __str__(self):
        return str(self.title)
    

