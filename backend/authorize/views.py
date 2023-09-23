from django.shortcuts import render


def home(request):

    return render(request, 'authorize/home.html', context={'title': 'Factory'})