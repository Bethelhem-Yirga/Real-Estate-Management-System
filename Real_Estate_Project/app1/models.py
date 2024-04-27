import datetime
from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.db import models
import re
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class Registration(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('customer', 'Customer'),
        ('admin', 'Admin'),
        ('finace', 'finace'),
        ('salesperson', 'Salesperson'),
        ('marketing_manager', 'Marketing Manager'),
        ('maintenance_staff', 'Maintenance Staff'),
        
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(8, message="Password must be at least 8 characters long.")
        ]
    )
    confirm_password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default='customer', choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    def clean(self):
        # Check if the first name contains only alphabetic characters without spaces
        if not self.first_name.replace(" ", "").isalpha():
            raise ValidationError("First name can only contain alphabetic characters without spaces.")

        # Check if the last name contains only alphabetic characters without spaces
        if not self.last_name.replace(" ", "").isalpha():
            raise ValidationError("Last name can only contain alphabetic characters without spaces.")

        # Check if the phone number contains only numeric characters without spaces
        if not self.phone_number.replace(" ", "").isdigit():
            raise ValidationError("Phone number can only contain numeric characters without spaces.")

        # Check if the email is already used
        if Registration.objects.filter(email=self.email).exists():
            raise ValidationError("Email is already in use.")

        # Check if the passwords match
        if self.password != self.confirm_password:
            raise ValidationError("Passwords do not match.")
     
     

MY_CHOICES = [
    ('For Sale', 'For Sale'),
    ('For Rent', 'For Rent'),
    ('Rented', 'Rented'),
    ('Soled', 'Soled'),
]

PROPERTY_CHOICES = [
        ('Commercial', 'Commercial'),
        ('Residential', 'Residential'),
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
    #date_added = models.DateTimeField(default=datetime.now, blank=True)
    year_built = models.IntegerField(blank=True, null=True)
    payment_link = models.URLField(max_length=200, blank=True, null=True)

    air_conditioning = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    lawn = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)

   # add_map = models.URLField(max_length=200, blank=True, null=True)
    
class Application(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=150)
    nationality = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    work_status= models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=100)
    partner_first_name = models.CharField(max_length=100, blank=True, null=True)
    partner_last_name = models.CharField(max_length=100, blank=True, null=True)
    partner_phone_number = models.CharField(max_length=150, blank=True, null=True)
    partner_work_status = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

class Maintenance(models.Model):
    email = models.EmailField()
    building_number = models.CharField(max_length=100)
    room_number = models.IntegerField()
    floor_number = models.IntegerField()
    type_of_maintenance = models.CharField(max_length=20)

class MarketingManager(Registration):
    image = models.ImageField(upload_to='images', default='avator.jpg')


class Employee(Registration):
    img = models.ImageField(upload_to='images')



from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
   
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Call custom validation methods for specific fields
        self.validate_email()
        self.validate_name()
        self.validate_subject()
        self.validate_message()

    def validate_email(self):
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValidationError("Please enter a valid email address.")

    def validate_name(self):
        if len(self.name) < 2:
            raise ValidationError("Name must be at least 2 characters long.")

    def validate_subject(self):
        if len(self.subject) < 5:
            raise ValidationError("Subject must be at least 5 characters long.")

    def validate_message(self):
        if len(self.message) < 10:
            raise ValidationError("Message must be at least 10 characters long.")

    def __str__(self):
        return self.subject
from django.db import models

class Maintenance(models.Model):
    email = models.EmailField()
    building_number = models.CharField(max_length=100)
    room_number = models.IntegerField()
    floor_number = models.IntegerField()
    type_of_maintenance = models.CharField(max_length=20)

    sent_status = models.BooleanField(default=False)

    def send_link(self):
        self.sent_status = True
        self.save()

    @staticmethod
    def get_maintenance_requests():
        return Maintenance.objects.filter(sent_status=False)

    def __str__(self):
        return f"Maintenance Request #{self.pk}"

class Report(models.Model):
    maintenance = models.OneToOneField(Maintenance, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=100)

    def complete_maintenance(self):
        self.staff_name = ""
        self.save()

class Applicationrent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=150)
    nationality = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    work_status= models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    
# models.py

# models.py in app1 directory
# models.py in app1 directory

from django.db import models


class Finance(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, related_name='Finance', default=0)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
   
    date_of_purchase = models.DateField()
    purchase_or_rent = models.CharField(max_length=10, choices=[('buy', 'Buy'), ('rent', 'Rent')])
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rent_duration = models.CharField(max_length=100, null=True, blank=True)
    def update_property_status(self, new_status):
        # Update the status of the associated property
        self.property.status = new_status
        self.property.save()
    def __str__(self):
        return f"{self.customer_name}'s Finance"

    
    
    
