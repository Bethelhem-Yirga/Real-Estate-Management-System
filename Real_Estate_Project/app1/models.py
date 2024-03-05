import datetime
from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.db import models
# Create your models here.
class Registration (models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     email = models.EmailField()
     gender = models.CharField(max_length=10)
     address = models.CharField(max_length=200)
     phone_number = models.CharField(max_length=20)
     password = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(8, message="Password must be at least 8 characters long.")
        ]
    )
     confirm_password = models.CharField(max_length=100)

     def clean(self):
        if self.password != self.confirm_password:
            raise ValidationError("Passwords do not match.")
     

MY_CHOICES = [
    ('For Sale', 'For Sale'),
    ('For Rent', 'For Rent'),
]

class Properties(models.Model):
    propertyType = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    size = models.FloatField()
    price = models.FloatField()
    status = models.CharField(max_length=20, choices=MY_CHOICES)
    noOfRooms = models.BigIntegerField()
    bedrooms = models.BigIntegerField()
    bathrooms = models.BigIntegerField()
    roomFloor = models.BigIntegerField()
    TotalFloor = models.BigIntegerField()
    image = models.ImageField(upload_to='images', default='bg1.jpg')
    date_added = models.DateTimeField(default=datetime.now, blank=True)


class MarketingManager(Registration):
    employee_id = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images', default='avator.jpg')

    
    