from django.shortcuts import render


def login_page(request):
    return render(request, 'authorization/login.html')


def registration_page(request):
    return render(request, 'authorization/registration.html')