from django.shortcuts import render



def index(request):
    return render(request, 'user_auth/index.html')

def login(request):
    return render(request, 'user_auth/login.html')

def registration(request):
    return render(request, 'user_auth/registration.html')