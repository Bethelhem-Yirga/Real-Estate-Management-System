from msilib.schema import Property
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from django.contrib import messages
from .models import Employee, MarketingManager, Registration
from .forms import ApplicationForRentForm, ApplicationForRentFormUp, ApplicationFormUp, ProfileForm, RegistrationForm 

from .forms import ContactForm, ProfileForm, RegistrationForm
from app1.forms import PropertyForm
import stripe
from django.conf import settings
from django import forms 
from django.shortcuts import render
import stripe
from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse

from datetime import datetime

from .models import Properties, Registration,Application,Maintenance


from .models import Properties, Registration,Applicationrent

from django.core.mail import send_mail
from Real_Estate_Project import settings
from .models import Registration
from django.contrib.auth.models import User  
from django.contrib import messages
from .models import MarketingManager
from .forms import PropertyForm
from .forms import EmployeeForm
from django.shortcuts import render
from django.core.mail import send_mail
from .models import ContactMessage
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Application
from .models import Maintenance, Report
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from .models import Maintenance, Report
from .forms import ApplicationForm

def accept_or_reject_application(request, application_id, decision):
    application = Application.objects.get(id=application_id)
    if decision == 'accept':
        # Process acceptance logic here
        send_email(application.id, application.email, application.first_name, decision)
    elif decision == 'reject':
        # Process rejection logic here
        send_email(application.id, application.email, application.first_name, decision)
    return redirect('manager')
def send_email(application_id, email, first_name, decision):
    subject = 'Application Status'
    message = f"Dear {first_name},\n\nYour application has been {decision}ed."
    sender = 'bethelyg909@gmail.com'  # Change to your email
    recipient = [email]
    send_mail(subject, message, sender, recipient)



def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        recipient = request.POST['recipient']
        myfile = request.FILES['myfile']

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email='giftrealestate24@gmail.com',
            to=[recipient],
        )
        email.attach(myfile.name, myfile.read(), myfile.content_type)
        email.send()

        return HttpResponseRedirect('/success/')  # Redirect to a success page

    return render(request, 'email_form.html')  # Render the email form templat


def home_view(request):
    return render(request,'home.html')

def loginn(request):
    return render(request,'loginn.html')

def property_listing(request):
    properties = Properties.objects.all()
    salespersons = Employee.objects.filter(role='salesperson')
    context = {'properties': properties, 'salespersons': salespersons}
    return render(request, 'home.html', context)


def property_listing_page(request):
    properties = Properties.objects.all()
    context = {'properties': properties}
    return render(request, 'property_listing.html', context)
    

def salespersons(request):
    salespersons = Employee.objects.filter(role='salesperson')
    context = {'salespersons': salespersons}
    return render(request, 'salespersons.html', context)

def adminn(request):
    return render(request, 'adminn.html')


def manager(request):
    data = Application.objects.all()
    return render(request, 'manager.html', {'data': data})
# views.py



def appform(request,property_id):
        

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        nationality = request.POST.get('nationality')
        address = request.POST.get('address')
        work_status = request.POST.get('work_status')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marriage_status')
        partner_first_name = request.POST.get('partner_first_name')
        partner_last_name = request.POST.get('partner_last_name')
        partner_phone_number = request.POST.get('partner_phone_number')
        partner_work_status = request.POST.get('partner_work_status') 
        

        # Create a new instance of the Application model and assign the form data
        application = Application(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            nationality=nationality,
            address=address,
            work_status=work_status,
            gender=gender,
            marital_status=marital_status,
            partner_first_name=partner_first_name,
            partner_last_name=partner_last_name,
            partner_phone_number=partner_phone_number,
            partner_work_status=partner_work_status,
            date_added=datetime.now()  # Set the current date and time
    


        )
        
        
    
    
    return render(request, 'appform.html')

def application_for_sale(request,property_id):
     property = Properties.objects.get(id=property_id)
     form = ApplicationForm()  # Initialize the form

     if request.method == 'POST':
        form = ApplicationForm(request.POST)  # Bind form data from POST request

        if form.is_valid():
            form.save()  # Save the form data as a new Application instance
            return redirect('property_listing')


     context = {
        'property': property,
        'form': form,  # Pass the form to the template context
    }
     return render(request, 'application_for_sale.html', context)


def application_for_rent(request,property_id):
     property = Properties.objects.get(id=property_id)
     form = ApplicationForRentForm()  # Initialize the form

     if request.method == 'POST':
        form = ApplicationForRentForm(request.POST)  # Bind form data from POST request

        if form.is_valid():
            form.save()  # Save the form data as a new Application instance
            return redirect('property_listing')


     context = {
        'property': property,
        'form': form,  # Pass the form to the template context
    }
     return render(request, 'application_for_rent.html', context)

def apptorent(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        nationality = request.POST.get('nationality')
        address = request.POST.get('address')
        work_status = request.POST.get('work_status')
        gender=request.POST.get('gender')
        
        # Create a new instance of the Application model and assign the form data
        applicationrent= Applicationrent (
             first_name=first_name,
             last_name=last_name,
             email=email,
             phone_number=phone_number,
             nationality=nationality,
             address=address,
             work_status=work_status,
             gender=gender,
             date_added=datetime.now()  # Set the current date and time


        )
        
        # Save the application instance to the database
        applicationrent.save()
    
    return render(request, 'apptorent.html')

        # Save the application instance to the database
def rent(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        building_number = request.POST.get('building_number')
        floor_number = request.POST.get('floor_number')
        room_number = request.POST.get('room_number')
        type_of_maintenance = request.POST.get('type_of_maintenance')

        maintenance_requests =Maintenance(
            email=email,
            building_number=building_number,
            floor_number=floor_number,
            room_number=room_number,
            type_of_maintenance=type_of_maintenance
        )
        maintenance.save()  # Redirect to a success page
    return render(request, 'rent.html')

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



def manager(request):
    applications = Application.objects.all()
    maintenance_requests = Maintenance.objects.all()
    contact=ContactMessage.objects.all()
    applicationrent =Applicationrent.objects.all()
    return render(request, 'manager.html', {'applications': applications,'applicationrent':applicationrent,'maintenance_requests': maintenance_requests})

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

def mrkMng(request):
    all_info = Properties.objects.all()
    total_properties = Properties.objects.count()
    sale_properties = Properties.objects.filter(status='For Sale').count()
    rent_properties = Properties.objects.filter(status='For Rent').count()
    soled_properties = Properties.objects.filter(status='Soled').count()
    rented_properties = Properties.objects.filter(status='Rented').count()
    marketing_manager_profile = Employee.objects.filter(role='marketing_manager').first()

    context = {
        'all_info': all_info,
        'total_properties': total_properties,
        'sale_properties': sale_properties,
        'soled_properties':soled_properties,
        'rent_properties': rent_properties,
        'rented_properties': rented_properties,
        'marketing_manager_profile':marketing_manager_profile
    }
    return render(request, 'mrk_mng.html', context)
   

def forsale(request):
    all_info = Properties.objects.all()
    total_properties = Properties.objects.count()
    sale_properties = Properties.objects.filter(status='For Sale').count()
    rent_properties = Properties.objects.filter(status='For Rent').count()
    soled_properties = Properties.objects.filter(status='Soled').count()
    rented_properties = Properties.objects.filter(status='Rented').count()
    marketing_manager_profile = Employee.objects.filter(role='marketing_manager').first()

    context = {
        'all_info': all_info,
        'total_properties': total_properties,
        'sale_properties': sale_properties,
        'rent_properties': rent_properties,
        'soled_properties':soled_properties,
        'rented_properties': rented_properties,
        'marketing_manager_profile':marketing_manager_profile
    }
    return render(request, 'forsale.html', context)

   

def forent(request):
    all_info = Properties.objects.all()
    total_properties = Properties.objects.count()
    sale_properties = Properties.objects.filter(status='For Sale').count()
    rent_properties = Properties.objects.filter(status='For Rent').count()
    soled_properties = Properties.objects.filter(status='Soled').count()
    rented_properties = Properties.objects.filter(status='Rented').count()
    marketing_manager_profile = Employee.objects.filter(role='marketing_manager').first()

    context = {
        'all_info': all_info,
        'total_properties': total_properties,
        'sale_properties': sale_properties,
        'rent_properties': rent_properties,
        'soled_properties':soled_properties,
        'rented_properties': rented_properties,
        'marketing_manager_profile':marketing_manager_profile
    }
    return render(request, 'forent.html', context)
   
def soled(request):
    all_info = Properties.objects.all()
    total_properties = Properties.objects.count()
    sale_properties = Properties.objects.filter(status='For Sale').count()
    rent_properties = Properties.objects.filter(status='For Rent').count()
    soled_properties = Properties.objects.filter(status='Soled').count()
    rented_properties = Properties.objects.filter(status='Rented').count()
    marketing_manager_profile = Employee.objects.filter(role='marketing_manager').first()

    context = {
        'all_info': all_info,
        'total_properties': total_properties,
        'sale_properties': sale_properties,
        'rent_properties': rent_properties,
        'soled_properties':soled_properties,
        'rented_properties': rented_properties,
        'marketing_manager_profile':marketing_manager_profile
    }
    return render(request, 'soled.html', context)

   
def rented(request):
    all_info = Properties.objects.all()
    total_properties = Properties.objects.count()
    sale_properties = Properties.objects.filter(status='For Sale').count()
    rent_properties = Properties.objects.filter(status='For Rent').count()
    soled_properties = Properties.objects.filter(status='Soled').count()
    rented_properties = Properties.objects.filter(status='Rented').count()
    marketing_manager_profile = Employee.objects.filter(role='marketing_manager').first()

    context = {
        'all_info': all_info,
        'total_properties': total_properties,
        'sale_properties': sale_properties,
        'rent_properties': rent_properties,
        'soled_properties':soled_properties,
        'rented_properties': rented_properties,
        'marketing_manager_profile':marketing_manager_profile
    }
    return render(request, 'rented.html', context)


   

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




def add_property(request):
    if request.method == 'POST':
        marketing_manager_profile = Employee.objects.filter(role='marketing_manager').first()
        form = PropertyForm(request.POST, request.FILES)

        context ={
            'marketing_manager_profile' : marketing_manager_profile,
             'form' : form, 
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Data added successfully.')
           # return redirect('property_list')  # Redirect to a success page or another view
        else:
            # Add form errors to Django messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {form[field].label}: {error}")
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', context)



def add_property(request):
    marketing_manager_profile = Employee.objects.filter(role='marketing_manager').first()
    form = PropertyForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Data added successfully.')
            
        else:
            # Add form errors to Django messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {form[field].label}: {error}")

    context = {
        'marketing_manager_profile': marketing_manager_profile,
        'form': form,
    }

    return render(request, 'add_property.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Properties
from .forms import PropertyForm
from .models import Employee

def update_property(request, property_id):
    marketing_manager_profile = Employee.objects.filter(role='marketing_manager').first()
    property_obj = get_object_or_404(Properties, id=property_id)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data updated successfully.')
            return redirect('mrk_mng')
    else:
        form = PropertyForm(instance=property_obj)

    context = {
        'marketing_manager_profile': marketing_manager_profile,
        'property_obj': property_obj,
        'form': form  # Include the form in the context to render it in the template
    }

    return render(request, 'update_property.html', context)

def property_detail(request, property_id):
    property_obj = get_object_or_404(Properties, id=property_id)
    return render(request, 'property_detail.html', {'property': property_obj})





def custemer(request):
    all_customers = Registration.objects.all()
    context = {'all_customers': all_customers}
    return render(request, 'custemer.html', context)



def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully.')
            return redirect('login')  # Redirect to the success page
    else:
        form = RegistrationForm()
    return render(request, 'registration_view.html', {'form': form})






def profile_view(request):
     mrk_mng_profile = Registration.objects.filter(role='marketing_manager').first()
     return render(request, 'mrk_mng_profile.html', {'mrk_mng_profile': mrk_mng_profile})




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

from django.shortcuts import render, redirect

from django.urls import reverse
from .models import Registration
from .models import Employee

from django.shortcuts import redirect, render
from .models import Registration  # Assuming Registration is your model for users

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Retrieve user from the database and validate credentials
        try:
            user = Registration.objects.get(email=email)
            if user.password == password and user.is_active:
                # Define a dictionary to map roles to page URLs
                role_page_map = {
                    'admin': 'system_admin',
                    'manager': 'manager_page',
                    'customer': 'property_listing',
                    'salesperson': 'salespersons',
                    'marketing_manager': 'mrk_mng',
                    'maintenance_staff': 'maintenance_staff_page',
                    'finance': 'https://dashboard.stripe.com/login'
                }
                # Check if the user's role is in the map
                if user.role in role_page_map:
                    # Redirect to the appropriate page based on the role
                    return redirect(role_page_map[user.role])
                else:
                    # If role is not found in the map, render failure page
                    return render(request, 'failure.html')
            else:
                # Password does not match or user is not active
                return render(request, 'failure.html')
        except Registration.DoesNotExist:
            # User does not exist
            return render(request, 'failure.html')

    return render(request, 'login.html')





"""def system_admin(request):

    employees = Employee.objects.all()
    total_employees = Employee.objects.count()
    salespersons = Employee.objects.filter(role='salesperson').count()
    maintenance_staff = Employee.objects.filter(role='maintenance_staff').count()
    
    context = {
        'employees': employees, 
        'admin_profile': admin_profile,
        'total_employees': total_employees,
        'salespersons': salespersons,
        'maintenance_staff': maintenance_staff

   }

    if True:
        admin_profile = Employee.objects.filter(role='admin').first()
        
    else:
        admin_profile = None
    return render(request, 'system_admin.html', context)
"""

def system_admin(request):
    employees = Employee.objects.all()
    total_employees = Employee.objects.count()
    salespersons = Employee.objects.filter(role='salesperson').count()
    maintenance_staff = Employee.objects.filter(role='maintenance_staff').count()
  
    admin_profile = Employee.objects.filter(role='admin').first()
  
    context = {
        'employees': employees, 
        'admin_profile': admin_profile,
        'total_employees': total_employees,
        'salespersons': salespersons,
        'maintenance_staff': maintenance_staff
    }

    return render(request, 'system_admin.html', context)

from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def add_employee(request):
    admin_profile = Employee.objects.filter(role='admin').first()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('system_admin')
    else:
        form = EmployeeForm()

    context = {
        'admin_profile': admin_profile,
        'form': form,
    }

    return render(request, 'add_employee.html', context)

def update_employee_active_status(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        is_active = request.POST.get('is_active', False)
        if is_active == 'true':  # Check if the checkbox is included in the form data
            employee.is_active = True
        else:
            employee.is_active = False
        employee.save()
        return redirect('system_admin')

    return render(request, 'update_employee_active_status.html', {'employee': employee})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employee_detail.html', {'employee': employee})

def system_admin_profile(request):
    admin_profile = Registration.objects.filter(role='admin').first()
    return render(request, 'system_admin_profile.html', {'admin_profile': admin_profile})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ChangePasswordForm

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('system_admin_profile')  
    else:
        form = ChangePasswordForm(request.user)
    
    return render(request, 'change_password.html', {'form': form})


def salesperson_profile(request, employee_id):
    salesperson = get_object_or_404(Employee, id=employee_id)
    context = {'salesperson': salesperson}
    return render(request, 'salesperson_profile.html', context)

def about(request):
    return render(request, 'about.html')





def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            #return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})







from django.shortcuts import render, redirect
from .models import Registration

from django.shortcuts import render, redirect
from .models import Registration

def logincustemer(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Retrieve user from the database and validate credentials
        try:
            user = Registration.objects.get(email=email)
            if user.password == password:
                # Email and password match
                return redirect('property_listing')  # Redirect to the desired page after successful login
            else:
                # Password does not match
                return render(request, 'failure.html')
        except Registration.DoesNotExist:
            # User does not exist
            return render(request, 'failure.html')

    return render(request, 'logincustemer.html')

def manager(request):
    maintenance_requests = Maintenance.objects.all()
    context = {'maintenance_requests': maintenance_requests}
    return render(request, 'manager.html', context)
def maintenance(request):
    maintenance_requests = Maintenance.objects.all()
    context = {'maintenance_requests': maintenance_requests}
    return render(request, 'maintenance.html', context)

def send_link(request, maintenance_id):
    maintenance_request = Maintenance.objects.get(pk=maintenance_id)
    maintenance_request.send_link()
    return redirect('manager')

def complete_maintenance(request, maintenance_id):
    maintenance_request = Maintenance.objects.get(pk=maintenance_id)
    if request.method == 'POST':
        staff_name = request.POST['staff_name']
        Report.objects.create(maintenance=maintenance_request, staff_name=staff_name)
        maintenance_request.complete_maintenance()
        return redirect('maintenance')
    context = {'maintenance_request': maintenance_request}
    return render(request, 'manager.html', context)






# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update the session to reflect the new password
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')  # Redirect to the user's profile page
        else:
            # If form is not valid, display errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

# views.py in app1 directory

from django.shortcuts import render, redirect
from .forms import FinanceForm

def finance_form(request):
    if request.method == 'POST':
        form = FinanceForm(request.POST)
        if form.is_valid():
            finance_instance = form.save(commit=False)
            finance_instance.property = form.cleaned_data['property_id']
            finance_instance.save()
            return redirect('finance_with_property_data')  # Redirect to a success page
    else:
        form = FinanceForm()
    return render(request, 'finance_form.html', {'form': form})

def success_page(request):
    return render(request, 'login.html')


# views.py in app1 directory
from .models import Finance


def finance_with_property_data(request):
  
    all_objects = Finance.objects.all()

    print(all_objects)  # Add this line for debugging
    return render(request, 'finance_with_property_data.html', {'finance_entries': all_objects})



# views.py

from django.http import JsonResponse
from .models import Finance

def finance_detail_api(request, finance_id):
    try:
        finance_entry = Finance.objects.get(id=finance_id)
        data = {
            'customer_name': finance_entry.customer_name,
            'customer_email': finance_entry.customer_email,
            'price': finance_entry.price,
            'remaining_amount': finance_entry.remaining_amount,
            'date_of_purchase': finance_entry.date_of_purchase,
            'property_size': finance_entry.property.size,
            'property_status': finance_entry.property.status,
            'number_of_rooms': finance_entry.property.noOfRooms,
            'bedrooms': finance_entry.property.bedrooms,
            'bathrooms': finance_entry.property.bathrooms,
            'room_floor': finance_entry.property.roomFloor,
            'total_floor': finance_entry.property.TotalFloor,
            'year_built': finance_entry.property.year_built,
            'property_price': finance_entry.property.price,
            'property_image': finance_entry.property.image.url,
            # Add more property-related fields as needed
        }
        return JsonResponse(data)
    except Finance.DoesNotExist:
        return JsonResponse({'error': 'Finance entry not found'}, status=404)

from django.shortcuts import render, get_object_or_404
from .models import Finance

def finance_detail_view(request, finance_id):
    finance_entry = get_object_or_404(Finance, id=finance_id)
    return render(request, 'finance_detail.html', {'finance_entry': finance_entry})


def mng(request):
    applications = Application.objects.all()
    applicationrent =Applicationrent.objects.all()
    total_properties = Properties.objects.count()
    sale_properties = Properties.objects.filter(status='For Sale').count()
    rent_properties = Properties.objects.filter(status='For Rent').count()
    soled_properties = Properties.objects.filter(status='Soled').count()
    rented_properties = Properties.objects.filter(status='Rented').count()
    marketing_manager_profile = Employee.objects.filter(role='marketing_manager').first()

    context = {
        'applications': applications,
        'applicationrent':applicationrent,
        'total_properties': total_properties,
        'sale_properties': sale_properties,
        'soled_properties':soled_properties,
        'rent_properties': rent_properties,
        'rented_properties': rented_properties,
        'marketing_manager_profile':marketing_manager_profile
        
    }
    return render(request, 'mng.html',context)

def mng_rent(request):
    applications = Application.objects.all()
    applicationrent =Applicationrent.objects.all()
    total_properties = Properties.objects.count()
    sale_properties = Properties.objects.filter(status='For Sale').count()
    rent_properties = Properties.objects.filter(status='For Rent').count()
    soled_properties = Properties.objects.filter(status='Soled').count()
    rented_properties = Properties.objects.filter(status='Rented').count()
    marketing_manager_profile = Employee.objects.filter(role='marketing_manager').first()

    context = {
        'applications': applications,
        'applicationrent':applicationrent,
        'total_properties': total_properties,
        'sale_properties': sale_properties,
        'soled_properties':soled_properties,
        'rent_properties': rent_properties,
        'rented_properties': rented_properties,
        'marketing_manager_profile':marketing_manager_profile
        
    }
    return render(request, 'mng_rent.html',context)

    
def application_detail(request, application_id):
    application_obj = get_object_or_404(Application, id=application_id)
    return render(request, 'application_detail.html', {'application_obj': application_obj})

def rent_application_detail(request, application_id):
    application_obj = get_object_or_404(Applicationrent, id=application_id)
    return render(request, 'rent_application_detail.html', {'application_obj': application_obj})

def update_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    if request.method == 'POST':
        form = ApplicationFormUp(request.POST, instance=application)
        if form.is_valid():
            application.status = form.cleaned_data['status']
            application.save()
            return redirect('mng')
    else:
        form = ApplicationFormUp(instance=application)

    return render(request, 'update_application.html', {'form': form})


def update_application_rent(request, application_id):
    application = get_object_or_404(Applicationrent, id=application_id)

    if request.method == 'POST':
        form = ApplicationForRentFormUp(request.POST, instance=application)
        if form.is_valid():
            application.status = form.cleaned_data['status']
            application.save()
            return redirect('mng_rent')
    else:
        form = ApplicationForRentFormUp(instance=application)

    return render(request, 'update_application_rent.html', {'form': form})

from django.shortcuts import render

"""def send_email_to(request, email):
    return render(request, 'send_email_to.html', {'email': email})"""""

from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

def send_email_to(request, email, payment_link,first_name):
    subject = 'Congratulations! Your Application Has Been Accepted.'
    name = email.split('@')[0]  # Extract the part before '@'
    name = name.split('.')[0]
    message = f"Dear [{first_name}],   We are delighted to inform you that your application for Gift real estate  has been accepted! Congratulations on this significant milestone. We look forward to working with you on this exciting venture.To facilitate the payment process and ensure a seamless experience, we have created a personalized payment link exclusively for you. You can conveniently make payments by clicking on the secure payment portal below: {payment_link}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('Email sent successfully')  # Return a response
    # Add any further logic or redirect the user to an appropriate page

def feedback(request):
    feedback = ContactMessage.objects.all()
    marketing_manager_profile = Employee.objects.filter(role='marketing_manager').first()

    context = {
        'feedback': feedback,
        'marketing_manager_profile':marketing_manager_profile
    }
    return render(request, 'feedback.html', context)
   
