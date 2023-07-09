from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.urls import reverse
from . import views
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
'''def user_login(request):
    return render(request, 'authentication/login.html')'''


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('polls')
            else:
                return redirect(form=LoginForm())
    else:
        return render(request, 'authentication/login.html', {})


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('polls:index'))


def show_user(request, username):
    user = User.objects.get(username=username)
    return render(request, 'authentication/user.html', {
        "username": user.username,
        "password": user.password
    })


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            user = User.objects.create_user(username=username, password=password, first_name=first_name)
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = RegistrationForm()

    return render(request, 'registration/registration.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('user_auth:login')
