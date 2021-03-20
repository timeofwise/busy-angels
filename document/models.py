from django.db import models

# Create your models here.

class Storage(models.Model):
    classify = models.CharField(max_length=20)
    title = models.CharField(max_length=80)
    desc = models.CharField(max_length=200)
    url = models.CharField(max_length=150)