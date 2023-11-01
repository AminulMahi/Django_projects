from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    messages = models.CharField(max_length=255)
    # CreatingVariable = ModelsMethod.DataType(Deafault or customizeable paramiter)