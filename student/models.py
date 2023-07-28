

# Create your models here.
from django.db import models

class student(models.Model):
    student_name = models.CharField(max_length=50, default="")
    Father_name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Age = models.IntegerField()
    Class = models.IntegerField(default="4")
    Mobile_no = models.IntegerField(default="1234567890")
    Gender = models.CharField(max_length=10, default="Other")
    paid_fees = models.IntegerField(default="0")
    due_fees = models.IntegerField(default="0")


    def __str__(self):
        return self.student_name

class fees(models.Model):
    Class = models.IntegerField(unique=True)
    fees = models.IntegerField()

    def __int__(self):
        return self.Class