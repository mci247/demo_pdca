from django.db import models
from  django.utils import  timezone

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    company = models.CharField(max_length=100, null=False, blank=False)
    time_create = models.DateTimeField(default=timezone.datetime.now())