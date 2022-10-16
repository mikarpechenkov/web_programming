from django import forms


class RegistrationForm(forms.Form):
    inputName = forms.CharField(required=True)
    inputSurname = forms.CharField(required=True)
    inputEmail = forms.EmailField(required=True)
    inputPassword = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'id': 'inputPassword', 'placeholder': 'password'}),
        required=True)

    inputName.widget.attrs['type'] = 'text'
    inputName.widget.attrs['class'] = 'form-control'
    inputName.widget.attrs['id'] = 'inputName'
    inputName.widget.attrs['placeholder'] = 'Name'

    inputSurname.widget.attrs['type'] = 'text'
    inputSurname.widget.attrs['class'] = 'form-control'
    inputSurname.widget.attrs['id'] = 'inputSurname'
    inputSurname.widget.attrs['placeholder'] = 'Surname'

    inputEmail.widget.attrs['class'] = 'form-control'
    inputEmail.widget.attrs['id'] = 'inputEmail'
    inputEmail.widget.attrs['placeholder'] = 'example@mail.ru'
