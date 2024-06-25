from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from .forms import ProductoForm
from .models import Producto
from django.utils import timezone

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
    if request.method == 'GET':
        return render(request,'myapp/Crear_Productos.html',{
            'form': ProductoForm
    })
    else:
        try:
            form = ProductoForm(request.POST)
            nuevo_Producto = form.save(commit=False)
            nuevo_Producto.user = request.user
            nuevo_Producto.save()
            return redirect('Productos')
        except ValueError:
            return render(request,'myapp/Crear_Productos.html',{
            'form': ProductoForm,
            'error': 'Por Favor proporciona datos validos'
    })


def Productos(request):
    Productos = Producto.objects.all()
    return render(request,'myapp/Productos.html',{'Productos': Productos})


def detalle_Producto(request, id_Producto):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, pk=id_Producto)
        form = ProductoForm(instance = producto)
        return render(request, 'myapp/detalle_Producto.html',
                  {'producto': producto,
                    'form'   : form 
                   })
    else:
        try:
            producto = get_object_or_404(Producto, pk=id_Producto)
            form = ProductoForm(request.POST, instance=producto)
            form.save()
            return redirect('Productos')
        except ValueError:
            return render(request, 'myapp/detalle_Producto.html',
                           {'producto':producto,
                           'form':form,
                            'error': ' Error al actualizar producto'
                            })

def Producto_completado (request, id_Producto):
    productos = get_object_or_404(Producto, pk=id_Producto, user=request.user)
    if request.method == 'POST':
        productos.fechaCompletada = timezone.now()
        productos.save()
        return redirect('Productos')


def signout(request):
    logout(request)
    return redirect('home')

