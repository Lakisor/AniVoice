from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'Voicer/home.html')

def registration(request):
    form = CreateUserForm
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            print(form.is_valid())
            print(form.errors)
            if form.is_valid():
                print('login')
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'account  ' + user)
                return redirect('home')
    context = {'form': form}

    return render(request, 'Voicer/registration.html', context)