from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.http import Http404
from django.core.paginator import Paginator
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'show')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'show': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


def create(request):
    
    if request.method == 'POST':
        context = {
        'form': ContactForm(data=request.POST),
        'site_title': 'Create Contact - ',
    }
        return render(
        request,
        'contact/create.html',
        context
    )
        
    context = {
        'form': ContactForm(),
        'site_title': 'Create Contact - ',
    }
    
    return render(
        request,
        'contact/create.html',
        context
    )
        
    

    
    