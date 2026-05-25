from django.shortcuts import render
from django import forms
from contact.forms import RegistrationForm
from django.contrib import messages

def register(request):
    form = RegistrationForm()
    
    messages.info(request, 'Please fill out the form to create an account.')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )