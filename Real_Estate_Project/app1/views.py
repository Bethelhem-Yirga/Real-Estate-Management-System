from django.shortcuts import render

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