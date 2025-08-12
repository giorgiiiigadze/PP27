from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile
from .forms import ContactForm, UserProfileForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


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
    else:
        form = ContactForm()
    return render(request, 'message/contact.html', {'form': form})


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user =  request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)

        p_form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=user_profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=user_profile)

    return render(request, 'users/profile.html', 
                  {'u_form':u_form, 'p_form':p_form})



