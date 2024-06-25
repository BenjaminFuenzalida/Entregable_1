from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError

def home(request):
    return render(request, 'myapp/home.html')


def contacto(request):
    return render(request, 'myapp/contacto.html')

def carro_de_compras(request):
    return render(request, 'myapp/carro_de_compras.html')

def pagina_en_mantencion(request):
    return render(request, 'myapp/pagina_en_mantencion.html')

def proceso_de_compras(request):
    return render(request, 'myapp/proceso_de_compras.html')


def sign_up(request):

    if request.method == 'GET':
        return render(request, 'myapp/sign_up.html', {
        'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #registrar usuario
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('sign_in')
            except IntegrityError:
                return render(request, 'myapp/sign_up.html', {
                    'form' : UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'myapp/sign_up.html', {
            'form' : UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def sign_in(request):
    if request.method == 'GET':
            return render(request, 'myapp/sign_in.html', {
        'form' : AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password']
        )

        if user is None:
            return render(request, 'myapp/sign_in.html', {
            'form' : AuthenticationForm,
            'error': 'El Usuario o la Contraseña es incorrecto :( '
        })
        else:
            login(request, user)
            return redirect('home')


def Crear_Producto(request):
    return render(request,'myapp/Crear_Productos.html')

def signout(request):
    logout(request)
    return redirect('home')

