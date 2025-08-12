from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Handle the message here
            # return redirect('thank_you')
    else:
        form = ContactForm()
    return render(request, 'message/contact.html', {'form': form})

