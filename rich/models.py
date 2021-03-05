from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Asset(models.Model):
    date = models.DateField(unique=True, null=True)

    # Present Value
    present_value_1 = models.IntegerField(default=0, null=True)
    present_value_2 = models.IntegerField(default=0, null=True)
    present_value_3 = models.IntegerField(default=0, null=True)
    present_value_4 = models.IntegerField(default=0, null=True)
    present_value_5 = models.IntegerField(default=0, null=True)
    present_value_6 = models.IntegerField(default=0, null=True)

    # Future Value
    future_value_1 = models.IntegerField(default=0, null=True)
    future_value_2 = models.IntegerField(default=0, null=True)
    future_value_3 = models.IntegerField(default=0, null=True)
    future_value_4 = models.IntegerField(default=0, null=True)
    future_value_5 = models.IntegerField(default=0, null=True)
    future_value_6 = models.IntegerField(default=0, null=True)

    class Meta:
        ordering = ['-date']
