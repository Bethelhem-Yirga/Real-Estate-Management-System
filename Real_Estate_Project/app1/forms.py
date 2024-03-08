from cProfile import Profile
from django import forms
from .models import MarketingManager, Properties,Registration
from django.conf import settings
import stripe

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields =['first_name','last_name','email','gender','address','phone_number','password','confirm_password']

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



