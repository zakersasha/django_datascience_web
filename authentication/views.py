from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Пользователь успешно зарегистрирован!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')

    else:
        form = UserRegisterForm()

    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_profile(request):
    return render(request, 'main/profile.html')
