from django.db import models

# Create your models here.

class user_data(models.Model):
    
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    video = models.ImageField(upload_to='video/')
