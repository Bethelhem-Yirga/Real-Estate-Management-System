from django import forms
from .models import Properties

"""class PropertiesForm(forms.ModelForm):  
    class Meta:  
        model = Properties  
        fields = "__all__" """

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = '__all__'      