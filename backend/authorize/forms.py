from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignInUserForm(AuthenticationForm):       # Форма авторизаций пользователя(Поля: логин, пароль)

    class Meta: 
        model = User
        fields = ('username', 'password')

    
    username = forms.CharField(label='Логин:', widget=forms.TextInput(attrs={
        'class': 'form-control py-1',
        'placeholder': 'Введите логин',
    }))

    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={
        'class': 'form-control py-1',
        'placeholder': 'Введите пароль',
    }))


class SignUpUserForm(UserCreationForm):         # Форма регистраций пользователя(Поля: логин, имя, пароль-1, пароль-2)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')


    first_name = forms.CharField(label='Имя:', widget=forms.TextInput(attrs={
        'class': 'form-control py-1',
        'placeholder': 'Введите имя',
    }))

    username = forms.CharField(label='Логин:', widget=forms.TextInput(attrs={
        'class': 'form-control py-1',
        'placeholder': 'Введите логин',
    }))

    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={
        'class': 'form-control py-1',
        'placeholder': 'Придумайте пароль',
    }))

    password2 = forms.CharField(label='Подтвердите пароль:', widget=forms.PasswordInput(attrs={
        'class': 'form-control py-1',
        'placeholder': 'Подтвердите пароль',
    }))