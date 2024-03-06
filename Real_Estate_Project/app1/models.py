import datetime
from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.db import models
import re
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator

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

PROPERTY_CHOICES = [
        ('Villa', 'Villa'),
        ('Apartment', 'Apartment'),
    ]
PROPERTY_AREA = [
        ('22 Mazoria', '22 Mazoria'),
        ('Atlas', 'Atlas'),
        ('Ayat site', 'Ayat site'),
        ('CMC site', 'CMC site'),
    ]
    
    
class Properties(models.Model):
    propertyType = models.CharField(max_length=100, choices=PROPERTY_CHOICES)
    country = models.CharField(max_length=100, default='Ethiopia', validators=[
        RegexValidator(
            regex=re.compile('^[A-Za-z\s]+$'),
            message='Country name should contain only alphabetic characters.',
            code='invalid_country'
        )
    ])
    city = models.CharField(max_length=100, default='Addis Ababa', validators=[
        RegexValidator(
            regex=re.compile('^[A-Za-z\s]+$'),
            message='City name should contain only alphabetic characters.',
            code='invalid_city'
        )
    ])
    area = models.CharField(max_length=100,choices=PROPERTY_AREA)
    description = models.TextField()
    size = models.FloatField(validators=[MinValueValidator(0.0)])
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    status = models.CharField(max_length=20, choices=MY_CHOICES)
    noOfRooms = models.BigIntegerField(validators=[MinValueValidator(0)])
    bedrooms = models.BigIntegerField(validators=[MinValueValidator(0)])
    bathrooms = models.BigIntegerField(validators=[MinValueValidator(0)])
    roomFloor = models.BigIntegerField(validators=[MinValueValidator(0)])
    TotalFloor = models.BigIntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='images', default='bg1.jpg')
    date_added = models.DateTimeField(default=datetime.now, blank=True)


class MarketingManager(Registration):
    employee_id = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images', default='avator.jpg')

    
    