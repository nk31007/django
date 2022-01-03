from django.db import models

# Create your models here.


class Employee(models.Model):
    eno = models.IntegerFiel()
    ename = models.models.CharField(max_length=50)
    esal = models.FloatField()
