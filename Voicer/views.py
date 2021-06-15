from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import CreateUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def home(request):
    return render(request, 'Voicer/home.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect("home")
                    else:
                        return HttpResponse('Отключенный аккаунт')
                else:
                    messages.info(request, 'Неверные имя пользователя или пароль')
        else:
            form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username') #тут например типо мы уже ввели данные, но надо ещё сделать саму обработку страницы логин
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Неверные имя пользователя или пароль')
    context = {}
    return render(request, 'registration/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/')



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


def usercab(request, username):
    context = {}
    return render(request, 'Voicer/usercab.html', context)