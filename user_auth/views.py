from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginForm, RegistrationForm


class CustomLoginView(LoginView):
    template_name = 'user_auth/login2.html'
    authentication_form = LoginForm

    def get_success_url(self) -> str:
        return reverse_lazy('index')


class RegistrationView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'user_auth/register.html'
    success_url = reverse_lazy('login')


def index(request):
    return render(request, 'user_auth/index.html')

def login(request):
    return render(request, 'user_auth/login.html')

def registration(request):
    return render(request, 'user_auth/register.html')