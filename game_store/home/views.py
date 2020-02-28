from contextlib import redirect_stderr
from struct import error
from urllib import request

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from data.models import Game, Image


# Create your views here.
def home(request):
    game = Game.objects.all()
    image = Image.objects.all()
    print(game)
    return render(request,
                  'index.html',
                  context={
                      'games': game,
                      'images': image
                  })


def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'))
        # group = Group.objects.get(name='public')
        # user.groups.add(group)
        user.save()

        return render(request, 'login.html')

    return render(request, 'signup.html')


def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home_member')
        else:

            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    return render(request, 'login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect('login')


def allgame(request):
    game = Game.objects.all()
    image = Image.objects.all()
    print(game)
    return render(request,
                  'allgame.html',
                  context={
                      'games': game,
                      'images': image
                  })


def details(request):
    return render(request, 'details.html')


def home_member(request):
    game = Game.objects.all()
    image = Image.objects.all()
    print(game)
    return render(request,
                  'index.html',
                  context={
                      'games': game,
                      'images': image
                  })


def details_member(request):
    return render(request, 'details.html')


def mygame(request):
    return render(request, 'mygame.html')
