from pyexpat.errors import messages
from django.shortcuts import redirect, render

from app1.forms import PropertiesForm
from .models import Properties, Registration

from django.core.mail import send_mail
from Real_Estate_Project import settings
from .models import Registration


def home_view(request):
    return render(request, 'home.html')

def registration_view(request):
    return render(request, 'registration.html')

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

"""def addProperty(request):  
    if request.method == "POST":  
        form = PropertiesForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                messages.success(request, 'Data added successfully.')  
                return render(request, 'marketing_manager.html')  
            except:  
                pass  
    else:  
        form = PropertiesForm()  
    return render(request,'add_property.html',{'form':form})  """

def addProperty(request):
    if request.method == "POST":
        form = PropertiesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Data added successfully.')
                #return render(request, 'marketing_manager.html')
            except:
                pass
    else:
        form = PropertiesForm()
    return render(request, 'add_property.html', {'form': form})

