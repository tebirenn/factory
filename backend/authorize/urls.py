from django.urls import path

from . import views

app_name = 'authorize'

urlpatterns = [
    path('', views.home, name='user-home'),
    path('signin/', views.SignInUser.as_view(), name='user-signin'),
    path('signup/', views.SignUpUser.as_view(), name='user-signup'),
    path('signout/', views.signout_user, name='user-signout'),
]