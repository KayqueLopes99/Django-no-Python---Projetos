from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
from django.http import Http404
from django import forms
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact

def create(request):
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        form = ContactForm(data=request.POST, files=request.FILES)
        
        context = {
        'form': form,
        'site_title': 'Create Contact - ',
        'form_action': form_action,
    }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
            
        return render(
        request,
        'contact/create.html',
        context
    )
        
    context = {
        'form': ContactForm(),
        'site_title': 'Create Contact - ',
        'form_action': form_action,
    }
    
    return render(
        request,
        'contact/create.html',
        context
    )
        
    
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', kwargs={'contact_id': contact_id})
    
    if request.method == 'POST':
        form = ContactForm(data=request.POST, instance=contact, files=request.FILES)
        
        context = {
        'form': form,
        'site_title': 'Update Contact - ',
        'form_action': form_action,
    }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
            
        return render(
        request,
        'contact/create.html',
        context
    )
        
    context = {
        'form': ContactForm(instance=contact),
        'site_title': 'Update Contact - ',
        'form_action': form_action,
    }
    
    return render(
        request,
        'contact/create.html',
        context
    )
    
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )