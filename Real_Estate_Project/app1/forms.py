from cProfile import Profile
from django import forms
from .models import MarketingManager, Properties,Registration

from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = '__all__'      

class ProfileForm(forms.ModelForm):
    class Meta:
        model = MarketingManager
        fields = ['first_name', 'last_name', 'email', 'image', 'address']

