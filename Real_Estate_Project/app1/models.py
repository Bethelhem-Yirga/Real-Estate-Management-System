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
from django.core.validators import EmailValidator



class Registration(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('customer', 'Customer'),
        ('admin', 'Admin'),
        ('finace', 'finace'),
        ('salesperson', 'Salesperson'),
        ('marketing_manager', 'Marketing Manager'),
        ('maintenance_staff/electrician', 'Maintenance Staff/electrician'),
        ('maintenance_staff/plumber', 'Maintenance Staff/plumber'),


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
    role = models.CharField(max_length=30, default='customer', choices=ROLE_CHOICES)
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




def validate_no_space(value):
    if ' ' in value:
        raise ValidationError("Kebele cannot contain spaces.")   

class Applicationrent(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, related_name='application', default=0)
    first_name = models.CharField(max_length=100,validators=[RegexValidator(r'^[A-Za-z]*$', message="First name should contain only alphabetic characters."),
                                      RegexValidator(r'^[^\s]+$',
                                                     message="First name should not contain spaces.")
                                  ])
    middle_name = models.CharField(max_length=100, 
                                   validators=[
                                       RegexValidator(r'^[A-Za-z]*$',
                                                      message="Middle name should contain only alphabetic characters."),
                                       RegexValidator(r'^[^\s]+$',
                                                      message="Middle name should not contain spaces.")
                                   ])
    last_name = models.CharField(max_length=100,
                                 validators=[
                                     RegexValidator(r'^[A-Za-z]*$',
                                                    message="Last name should contain only alphabetic characters."),
                                     RegexValidator(r'^[^\s]+$',
                                                    message="Last name should not contain spaces.")
                                 ])
    
    phone_number = models.CharField(max_length=150,
                                    validators=[RegexValidator(r'^\d{10,15}$',
                                                               message="Phone number should be 10 to 15 digits.")])

    email = models.EmailField(validators=[EmailValidator(message="Enter a valid email address.")])
    def clean(self):
      
        super().clean()

        # Check if there is another application with the same email
        if Applicationrent.objects.filter(email=self.email).exclude(id=self.id).exists():
            raise ValidationError("This email is already being used by another application.")
        
    city = models.CharField(
        max_length=200,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='City name can only contain letters.',
                code='invalid_city_name'
            )
        ]
    ) 
    def clean(self):
        self.city = self.city.lstrip()
        super().clean()   
    sub_city = models.CharField(max_length=200, default="sub city",
            validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Sub City name can only contain letters .',
                code='invalid_sub_city_name'
            )
        ]                     
                                
    )
    def clean(self):
        self.city = self.city.lstrip()
        super().clean()
    kebele = models.CharField(
        max_length=200,
        default="Kebele",
        validators=[validate_no_space]
    )
    WORK_CHOICES = [
        ('Employed', 'Employed'),
        ('Self-employed', 'Self-employed'),
        
    ]
    work_status= models.CharField(max_length=100, choices= WORK_CHOICES)
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        
    ]
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
 

        

     

class Application(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, related_name='application_sale', default=0)

    first_name = models.CharField(max_length=100, validators=[
        RegexValidator(r'^[A-Za-z]*$', message="First name should contain only alphabetic characters."),
        RegexValidator(r'^[^\s]+$', message="First name should not contain spaces.")
    ])
    middle_name = models.CharField(max_length=100, default="middle name", validators=[
        RegexValidator(r'^[A-Za-z]*$', message="Middle name should contain only alphabetic characters."),
        RegexValidator(r'^[^\s]+$', message="Middle name should not contain spaces.")
    ])
    last_name = models.CharField(max_length=100, validators=[
        RegexValidator(r'^[A-Za-z]*$', message="Last name should contain only alphabetic characters."),
        RegexValidator(r'^[^\s]+$', message="Last name should not contain spaces.")
    ])
    email = models.EmailField(validators=[EmailValidator(message="Enter a valid email address.")])

    phone_number = models.CharField(max_length=150, validators=[
        RegexValidator(r'^\d{10,15}$', message="Phone number should be 10 to 15 digits.")
    ])

    NATIONALITY_CHOICES = [
        ('Ethiopian', 'Ethiopian'),
        ('Other', 'Other'),
    ]
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, default='Ethiopian')

    city = models.CharField(
        max_length=200,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='City name can only contain letters.',
                code='invalid_city_name'
            )
        ]
    )

    sub_city = models.CharField(
        max_length=200,
        default="sub city",
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Sub City name can only contain letters.',
                code='invalid_sub_city_name'
            )
        ]
    )

    kebele = models.CharField(
        max_length=200,
        default="Kebele",
        validators=[validate_no_space]
    )

    WORK_CHOICES = [
        ('Employed', 'Employed'),
        ('Self-employed', 'Self-employed'),
    ]
    work_status = models.CharField(max_length=100, choices=WORK_CHOICES)

    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
    ]
    marital_status = models.CharField(max_length=100, choices=MARITAL_STATUS_CHOICES)

    partner_first_name = models.CharField(max_length=100, blank=True, null=True, validators=[
        RegexValidator(r'^[A-Za-z]*$', message="First name should contain only alphabetic characters."),
        RegexValidator(r'^[^\s]+$', message="Partner First name should not contain spaces.")
    ])

    partner_last_name = models.CharField(max_length=100, blank=True, null=True, validators=[
        RegexValidator(r'^[A-Za-z]*$', message="First name should contain only alphabetic characters."),
        RegexValidator(r'^[^\s]+$', message="Partner Last name should not contain spaces.")
    ])

    partner_phone_number = models.CharField(max_length=150, blank=True, null=True, validators=[
        RegexValidator(r'^\d{10,15}$', message="Phone number should be 10 to 15 digits.")
    ])

    partner_work_status = models.CharField(max_length=100, blank=True, null=True, choices=WORK_CHOICES)

    date_added = models.DateTimeField(default=datetime.now, blank=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


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
"""
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
"""
    

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



# models.py in app1 directory
# models.py in app1 directory

from django.db import models


from django.db import models


class Finance(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, related_name='finance', default=0)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    date_of_purchase = models.DateField()
    purchase_or_rent = models.CharField(max_length=10, choices=[('buy', 'Buy'), ('rent', 'Rent')])
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rent_duration = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Get the associated property
        associated_property = self.property

        # Update the status of the associated property based on the status in the Properties model
        if associated_property.status == 'For Sale' :
            associated_property.status = 'Sold'
        elif associated_property.status == 'For Rent':
            associated_property.status = 'Rented'

        # Save the updated status of the property
        associated_property.save()

        # Call the super save method to save the finance instance
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name}'s Finance"



class AskMaintenance(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, related_name='askmaintenance',null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='askmaintenance_employee',null=True, blank=True)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='askmaintenance_registration',null=True, blank=True)
    
    SERVICE_CHOICES = [
        ('Electrical', 'Electrical'),
        ('Plumbing', 'Plumbing'),
    ]
    service=models.CharField(max_length=50, choices=SERVICE_CHOICES,default='Electrical Maintenance')
    
 
        
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
        
    date_added = models.DateTimeField(default=datetime.now, blank=True)

from django.db import models

class Salesperson(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, related_name='salespersons', default=0)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='salespersons', null=True, blank=True)
    date_of_markate = models.DateField()

    def __str__(self):
        return f"Salesperson - ID: {self.id}"
        '''
from django.shortcuts import render, redirect, get_object_or_404
from .models import Salesperson, Registration, Finance

def insert_salesperson_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        property_id = request.POST.get('property_id')
        
        # Check if the email belongs to an employee with the role of salesperson
        registration = get_object_or_404(Registration, email=email, role='salesperson')
        
        # Get the finance information based on the property ID
        finance = get_object_or_404(Finance, property__id=property_id)
        
        # Create a new Salesperson instance
        salesperson = Salesperson.objects.create(
            registration=registration,
            property=finance.property,
            date_of_markate=finance.date
        )
        
        # Optionally, you can redirect to a success page or render a success message
        return redirect('success_page_url')  # Replace 'success_page_url' with the URL of your success page
        
    return render(request, 'insert_salesperson.html')
    ''' 
    
