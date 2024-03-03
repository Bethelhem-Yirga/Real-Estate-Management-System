from django import forms
from .models import Properties,Registration

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


