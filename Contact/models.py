from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.TextField()
    country=models.TextField()
    msg=models.TextField()