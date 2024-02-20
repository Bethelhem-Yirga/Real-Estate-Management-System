from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def registration_view(request):
    return render(request, 'registration.html')