from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
class client:
    id:str
    name:str