from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'complaint_type', 'subject', 'description']

from django import forms
from .models import UserRegistration  # Assuming you have a User model

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['username', 'email', 'password']  # Add other fields as necessary
        widgets = {
            'password': forms.PasswordInput(),
        }
