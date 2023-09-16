from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserProfileForm(AuthenticationForm):
    username = forms.CharField(max_length=256,
                               label="Login",
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Введите имя пользователя'})
                               )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
