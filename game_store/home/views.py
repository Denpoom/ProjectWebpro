from contextlib import redirect_stderr
from struct import error
from urllib import request

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from data.models import User


# Create your views here.
def home(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')


def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('homelogin')
        else:

            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    return render(request, 'login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect('login')


def allgame(request):
    return render(request, 'allgame.html')


# def homemember(request):
#     return render(request, 'homemember.html')
def homelogin(request):
    return render(request, 'index.html')
