from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50)
    img_src = models.CharField(max_length=300)
    sex = models.IntegerField()
    bdate = models.CharField(max_length=30, default='undefined')

class HoroscopeModel(models.Model):
    description = models.CharField(max_length=1000)
    sign = models.CharField(max_length=20)
    start_date = models.CharField(max_length=20)