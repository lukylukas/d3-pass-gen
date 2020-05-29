from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'gen/home.html')

def bulma(request):
    return render(request, 'gen/bulma.html')

def password(request):

    thepassword= 'testing'

    characters=list('qwertyuiopasdfghjklzxcvbnm')
    theupper='not'
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*-=+'))

    lenght= int(request.GET.get('lenght'))

    thepassword= ''
    for x in range(lenght):
        thepassword+= random.choice(characters)

    return render(request, 'gen/password.html', {'password':thepassword})

def about(request):
    return render(request, 'gen/about.html')
