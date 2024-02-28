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
     
class Properties (models.Model):
    propertyType = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    size = models.BigIntegerField()
    price = models.BigIntegerField()
    status = models.BooleanField()
    noOfRooms = models.BigIntegerField()
    bedrooms = models.BigIntegerField()
    bathrooms = models.BigIntegerField()
    roomFloor = models.BigIntegerField()
    TotalFloor = models.BigIntegerField()
    image = models.ImageField(upload_to='imagess', default='bg1.jpg')  
