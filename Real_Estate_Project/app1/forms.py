from cProfile import Profile
import re
from django import forms
from .models import Application, Applicationrent, Employee, MarketingManager, Properties,Registration,ContactMessage
from django.conf import settings
import stripe


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields =['first_name','last_name','email','address','phone_number','password','confirm_password']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = '__all__'      

class ProfileForm(forms.ModelForm):
    class Meta:
        model = MarketingManager
        fields = ['first_name', 'last_name','image']



class PaymentForm(forms.Form):
    # Define your form fields here

    def process_payment(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Create a Stripe session and return the session ID
        session = stripe.Checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'name': 'Product Name',
                'description': 'Product Description',
                'amount': 1000,  # Amount in cents
                'currency': 'usd',
                'quantity': 1,
            }],
            success_url='https://example.com/success/',
            cancel_url='https://example.com/cancel/',
        )
        return session.id



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' 

from django import forms



from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(PasswordChangeForm):
    pass



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','last_name', 'email', 'subject', 'message']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

class ApplicationForRentForm(forms.ModelForm):
    class Meta:
        model = Applicationrent
        fields = '__all__'
        
        
 # forms.py in app1 directory

# forms.py in app1 directory
# forms.py in app1 directory

from django import forms
from .models import Finance
  # Adjust the import path based on your project structure

class FinanceForm(forms.ModelForm):
    property_id = forms.IntegerField()  # Field for entering property ID

    class Meta:
        model = Finance
        fields = ['property_id', 'customer_name', 'customer_email', 'price', 'date_of_purchase', 'remaining_amount', 'rent_duration']

    def clean_property_id(self):
        property_id = self.cleaned_data['property_id']
        try:
            property_obj = Properties.objects.get(pk=property_id)
        except Properties.DoesNotExist:
            raise forms.ValidationError("Property ID does not exist")
        return property_obj





        
        
        
        
        
        
