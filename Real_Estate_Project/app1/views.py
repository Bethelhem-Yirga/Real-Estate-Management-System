from django.shortcuts import render
from django.core.mail import send_mail

from Real_Estate_Project import settings

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