from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignInUserForm(AuthenticationForm):       # Форма авторизаций пользователя(Поля: логин, пароль)

    class Meta: 
        model = User
        fields = ('username', 'password')

    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4 form-input',
        'placeholder': 'Введите логин',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4 form-input',
        'placeholder': 'Введите пароль',
    }))


class SignUpUserForm(UserCreationForm):         # Форма регистраций пользователя(Поля: логин, имя, пароль-1, пароль-2)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')


    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4 form-input',
        'placeholder': 'Введите имя',
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4 form-input',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4 form-input',
        'placeholder': 'Придумайте пароль',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4 form-input',
        'placeholder': 'Подтвердите пароль',
    }))