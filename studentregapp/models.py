from django.db import models

class register(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    joiningdate=models.DateField()
    contact=models.CharField(max_length=11)
    email=models.EmailField()
    gender=models.CharField(max_length=255)
    qualification=models.CharField(max_length=255)
    
   