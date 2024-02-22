from django.shortcuts import render
<<<<<<< HEAD
from .models import Registration
=======
from django.core.mail import send_mail

from Real_Estate_Project import settings

>>>>>>> 0826b7d9dc44587e6a74d74bdb762219d9f3bb99
def home_view(request):
    return render(request, 'home.html')

def registration_view(request):
    return render(request, 'registration.html')

def property_listing(request):
    return render(request, 'property_listing.html')

def salespersons(request):
    return render(request, 'salespersons.html')

#def contact(request):
    #return render(request, 'contact.html')

def adminn(request):
    return render(request, 'adminn.html')

<<<<<<< HEAD
def custemer(request):
    all_custemers = Registration.objects.all()  # Correct the variable name
    context = {'all_custemers': all_custemers}  # Correct the syntax for creating a dictionary
    return render(request, 'custemer.html', context)
=======
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
            #[settings.EMAIL_HOST_USER],
            [receiver_email], 
            fail_silently=False,
        )

        settings.EMAIL_HOST_USER = 'bethelyg909@gmail.com'
        
        return render(request, 'contact_success.html')
   
    
    return render(request, 'contact.html')
>>>>>>> 0826b7d9dc44587e6a74d74bdb762219d9f3bb99
