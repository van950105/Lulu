from django.db import models

# Create your models here.

class InterestInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    hearFrom = models.CharField(max_length=50)
    comments = models.CharField(max_length=50)
