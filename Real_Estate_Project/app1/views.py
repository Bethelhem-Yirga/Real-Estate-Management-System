
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from django.contrib import messages
from .models import Registration
from .forms import RegistrationForm
from app1.forms import PropertyForm

from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse

from .models import Properties, Registration

from django.core.mail import send_mail
from Real_Estate_Project import settings
from .models import Registration
from django.contrib.auth.models import User  
from django.contrib import messages


def home_view(request):
    return render(request, 'home.html')

"""def registration_view(request):
    if request.method == 'POST':
        # Extract form data from the request
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        username = request.POST['username']
        address = request.POST['address']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        
        # Create a new user using create_user method
        myuser = User.objects.create_user(username, email, password)
        
        # Assign additional fields to the user object
        myuser.first_name = firstName
        myuser.last_name = lastName
        
        # Save the user object to the database
        myuser.save()
        
        # Display success message
        messages.success(request, "Registration successful")
        
        # Redirect the user to the home page
        return redirect('home')

    # Handle GET request or other request methods here
    # For example, you can render a registration form
    return render(request, 'registration.html')"""

def property_listing(request):
    return render(request, 'property_listing.html')

def salespersons(request):
    return render(request, 'salespersons.html')

def adminn(request):
    return render(request, 'adminn.html')
def appform(request):
    return render(request, 'appform.html')
def addemploy(request):
    return render(request, 'addemploy.html')
def rent(request):
    return render(request, 'rent.html')
def buy(request):
    return render(request, 'buy.html')
def custemer(request):
    
    all_custemers = Registration.objects.all()  # Correct the variable name
    context = {'all_custemers': all_custemers}  # Correct the syntax for creating a dictionary
    return render(request, 'custemer.html', context)


def manage(request):
    return render(request, 'manage.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        settings.EMAIL_HOST_USER = email

        receiver_email = "giftrealestate24@gmail.com"
        send_mail(
            subject,
            f"Name: {name}\nEmail: {email}\n\n{message}",
            email,
            [receiver_email],
            fail_silently=False,
        )

        settings.EMAIL_HOST_USER = 'bethelyg909@gmail.com'

        return render(request, 'contact_success.html')

    return render(request, 'contact.html')

def marketing_manager(request):
    return render(request, 'marketing_manager.html')

def custemer(request):
    all_customers = Registration.objects.all()
    context = {'all_customers': all_customers}
    return render(request, 'custemer.html', context)

def properties(request):
   all_info = Properties.objects.all()
   context = {'all_info':all_info}
   return render(request,"marketing_manager.html",context = context)


from .forms import PropertyForm

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data added successfully.')
            #return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})


def update_property(request, property_id):
    property_obj = get_object_or_404(Properties, id=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            form.save()
            return redirect('marketing_manager') 
    else:

        form = PropertyForm(instance=property)

        form = PropertyForm(instance=property_obj)

    return render(request, 'update_property.html', {'form': form})



 





def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully.')
    else:
        form = RegistrationForm()
    return render(request, 'registration_view.html', {'form': form})

def property_detail(request, property_id):
    property_obj = get_object_or_404(Properties, id=property_id)
    return render(request, 'property_detail.html', {'property': property_obj})

