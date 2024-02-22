from django.db import models

# Create your models here.
class Registration (models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     email = models.EmailField()
     gender = models.CharField(max_length=10)
     address = models.CharField(max_length=200)


     def __str__(self):
        return (self. first_name+ " "+ self. last_name)