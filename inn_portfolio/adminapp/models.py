from django.db import models

# Create your models here.


class Main(models.Model):
    name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=600)
    image = models.ImageField(upload_to='images/')
    f_url = models.URLField()
    l_url = models.URLField()
    t_url = models.URLField()
    g_url = models.URLField()

class Experience(models.Model):
    heading = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    date = models.DateField()

class Education(models.Model):
    u_name = models.CharField(max_length=100)
    u_title = models.CharField(max_length=100)
    u_subject = models.CharField(max_length=100)
    u_gpa = models.FloatField()
    u_date = models.DateField()

class Interest(models.Model):
    interest = models.TextField(max_length=700)

class Awards(models.Model):
    awards = models.CharField(max_length=100)

class Skills(models.Model):
    image = models.ImageField(upload_to='images/')
    workflow = models.CharField(max_length=255)