from django.shortcuts import render
from .models import Registration
def home_view(request):
    return render(request, 'home.html')

def registration_view(request):
    return render(request, 'registration.html')

def property_listing(request):
    return render(request, 'property_listing.html')

def salespersons(request):
    return render(request, 'salespersons.html')

def contact(request):
    return render(request, 'contact.html')
def adminn(request):
    return render(request, 'adminn.html')

def custemer(request):
    all_custemers = Registration.objects.all()  # Correct the variable name
    context = {'all_custemers': all_custemers}  # Correct the syntax for creating a dictionary
    return render(request, 'custemer.html', context)