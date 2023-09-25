from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view, permission_classes
from django.urls import reverse_lazy
import os
import requests

from .forms import *
from .models import *
from .serializers import *


class HomeAPIView(APIView):
    def get(self, request):
        context = {
            'title': 'Factory',
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
    def post(self, request):
        try: 
            username = request.data['username']
            tg_id = request.data['tg_id']

            user = User.objects.get(username=username)
            user.tg_id = tg_id
            user.save()
            return Response({'detail': 'success'}, status=200)
        except:
            return Response({'detail': 'user not found'}, status=404)
        

class SendMessageAPIView(APIView):

    def post(self, request):
        try:
            username = request.user.username
            tg_id = request.user.tg_id
            if not tg_id:
                return Response({'detail': 'set telegtam id'}, status=404)

            message_text = request.data['messageText']
            URL = f'https://api.telegram.org/bot{os.environ.get("BOT_TOKEN")}/sendMessage'
            bot_message = f'<b>{username}</b>, я получил от тебя сообщение:\n\n{message_text}'

            requests.post(URL, {'parse_mode': 'html', 'chat_id': tg_id, 'text': bot_message})

            return Response({'detail': 'Message sended'}, status=200)
        except:
            return Response({'detail': 'Message send error'}, status=404)
    

class UserDetailAPIView(RetrieveAPIView):
    
    def get_queryset(self):
        return User.objects.get(id=self.request.user.id)
    
class UserViewSet(GenericViewSet, mixins.CreateModelMixin, ):
    def get_queryset(self):
        if self.action == 'retrieve':
            return User.objects.get(id=self.request.user.id)
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'retrieve':
            return UserRetrieveSerializer
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


def signout_user(request):
    logout(request)
    return redirect('authorize:user-signin')