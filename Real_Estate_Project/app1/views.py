from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from django.contrib import messages
from .models import MarketingManager, Registration
from .forms import ProfileForm, RegistrationForm
from app1.forms import PropertyForm
import stripe
from django.conf import settings
from django import forms 
from django.shortcuts import render
import stripe
from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
from .models import Properties, Registration
from django.core.mail import send_mail
from Real_Estate_Project import settings
from .models import Registration
from django.contrib.auth.models import User  
from django.contrib import messages
from .models import MarketingManager


def home_view(request):
    return render(request, 'home.html')

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
    all_custemers = Registration.objects.all()  
    context = {'all_custemers': all_custemers}  
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
    profile = MarketingManager.objects.first()
    all_info = Properties.objects.all()
    total_properties = Properties.objects.count()
    sale_properties = Properties.objects.filter(status='For Sale').count()
    rent_properties = Properties.objects.filter(status='For Rent').count()

    context = {
        'all_info': all_info,
        'profile': profile,
        'total_properties': total_properties,
        'sale_properties': sale_properties,
        'rent_properties': rent_properties
    }
    return render(request, 'marketing_manager.html', context)


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

def profile_view(request):
    profile = MarketingManager.objects.first() 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()        
    else:
        form = ProfileForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile.html', context)











# views.py




def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            session_id = form.process_payment()
            return render(request, 'success.html', {'session_id': session_id})
    else:
        form = PaymentForm()
    
    return render(request, 'payment.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

class PaymentForm(forms.Form):
    # Define your form fields here

    def process_payment(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Create a Stripe session and return the session ID
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': 1000,
                    'product_data': {
                        'name': 'Product Name',
                        'description': 'Product Description',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success/',
            cancel_url='https://example.com/cancel/',
        )
        return session.id








from django.shortcuts import render
from .models import Registration

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Retrieve user from the database and validate credentials
        try:
            user = Registration.objects.get(email=email)
            if user.password == password:
                return render(request, 'success.html')
            else:
                return render(request, 'failure.html')
        except Registration.DoesNotExist:
            return render(request, 'failure.html')

    return render(request, 'login.html')

