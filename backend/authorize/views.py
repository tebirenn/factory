from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy

from .forms import *
from .models import *


@login_required(login_url='signin/', redirect_field_name=None)
def home(request):
    context = {
        'title': 'Factory'
    }

    return render(request, 'authorize/home.html', context=context)


class SignInUser(LoginView):
    form_class = SignInUserForm
    template_name = 'authorize/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'

        return context
    
    
    def get_success_url(self):
        return reverse_lazy('authorize:user-home')


class SignUpUser(CreateView):
    template_name = 'authorize/register.html'
    form_class = SignUpUserForm
    success_url = reverse_lazy('authorize:user-signin')


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'

        return context
    

class SetTgIdAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try: 
            username = request.data['username']
            tg_id = request.data['tg_id']

            user = User.objects.get(username=username)
            user.tg_id = tg_id
            user.save()
            return Response({'detail': 'success'}, status=200)
        except:
            return Response({'data': 'user not found'}, status=404)
    

def signout_user(request):
    logout(request)
    return redirect('authorize:user-signin')