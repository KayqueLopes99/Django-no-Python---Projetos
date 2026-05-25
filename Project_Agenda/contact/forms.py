from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email 
from . import models
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
 
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture')

    
    def _validate_name(self, value, field_name):
        if not value or len(value) < 2:
            raise ValidationError(f'{field_name.replace("_", " ").capitalize()} must have at least 2 characters.')
        return value

    def clean_first_name(self):
        return self._validate_name(self.cleaned_data.get('first_name'), 'first_name')

    def clean_last_name(self):
        return self._validate_name(self.cleaned_data.get('last_name'), 'last_name')

    def clean(self): 
        cleaned_data = self.cleaned_data
        first = cleaned_data.get('first_name')
        last = cleaned_data.get('last_name')
        
        if first and last and first == last:
            msg = 'First name and last name cannot be the same.'
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        return super().clean()

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        phone_clean = re.sub(r'[^0-9]', '', phone)

        if not (10 <= len(phone_clean) <= 11):
            raise ValidationError('Phone must have between 10 and 11 digits.')

        if not re.match(r'^[1-9]{2}9?[0-9]{8}$', phone_clean):
            raise ValidationError('Invalid phone number format.')

        return phone_clean

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower().strip()

        validate_email(email)

        allowed_domains = [
            'gmail.com',
            'hotmail.com',
            'outlook.com',
            'yahoo.com',
            'yahoo.com.br',
        ]

        domain = email.split('@')[-1]

        if domain not in allowed_domains:
            raise ValidationError(
                'Email domain not allowed.'
            )

        return email
    
    def clean_description(self):
        description = self.cleaned_data.get('description', '').strip()

        if not description:
            raise ValidationError('Description is required.')

        if len(description) < 10:
            raise ValidationError('Description must be at least 10 characters long.')

        return description
    

class RegistrationForm(UserCreationForm):
    
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Email is already in use.', code='invalid')
            )

        return email
