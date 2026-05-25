from django.shortcuts import render, redirect
from django import forms
from contact.forms import RegistrationForm, RegisterUpdateForm
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegistrationForm()
    
    if request.method == 'POST':
        
        form = RegistrationForm(request.POST)

        if form.is_valid():
            
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
    
def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'You have logged in successfully!')
            return redirect('contact:index')
        messages.error(request, 'Invalid username or password.')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')


@login_required
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('contact:user_update')
