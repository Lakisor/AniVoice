from django.core import paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import CreateUserForm, LoginForm, EditingUserForm, EdititngUserPasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    return render(request, 'registration/registration.html', context)

"""
блок с данными пользователя (начало) 
"""
def usercab(request, username):
    context = {}
    return render(request, 'profile/usercab.html', context)

#измененеие ника
def editusername(request, username):
    if request.method == 'POST':
        #объявляем первую переменую "form" если она нам нужна 
        form = EditingUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        #во всех остальных случаях будем брать образец юзера кекв
        form = EditingUserForm(instance=request.user)
    context = {"form":form}
    return render(request, 'profile/editingusername.html', context)

#изменение пароля
def editpassword(request, username):
    #тоже самое только для пароля
    if request.method == 'POST':
            #объявляем первую переменую "form" если она нам нужна 
        form = PasswordChangeForm(request.POST, user = request.user)
        print(form.is_valid())
        print(form.error_messages)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        #во всех остальных случаях будем брать образец юзера кекв
        form = PasswordChangeForm(user = request.user)
        
    context = {"form":form}
    return render(request, 'profile/editingpassword.html', context)

"""
блок с данными пользователя (конец) 
"""


def anime_list(request):
    object_list = Anime.objects.all().order_by('title')
    p = Paginator(object_list, 27)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    except PageNotAnInteger:
        page = p.page(1)
        
    return render(request, 'Voicer/animes.html', context={'animes':page})

