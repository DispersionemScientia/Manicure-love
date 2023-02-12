from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=250, label='Адрес электронной почты')
    first_name = forms.CharField(max_length=250, label='Имя')
    last_name = forms.CharField(max_length=250, label='Фамилия')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'birth_date', 'telephon_number']
        labels = {'username': 'Имя пользователя'}

class ChangeUserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'birth_date', 'telephon_number']
