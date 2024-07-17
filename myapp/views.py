from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from .forms import ProductoForm
from .models import Producto, Carrito, producto_item
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

def is_superuser (user):
    return user.is_superuser

def home(request):
    return render(request, 'myapp/home.html')

def contacto(request):
    return render(request, 'myapp/contacto.html')

def pagina_en_mantencion(request):
    return render(request, 'myapp/pagina_en_mantencion.html')



#------------- Session --------------------#

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'myapp/sign_up.html', {
        'form' : UserCreationForm
        })
    else:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            try:
                validate_password(password1)
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('sign_in')
            except ValidationError as e:
                return render(request, 'myapp/sign_up.html', {
                    'form': UserCreationForm(),
                    'error': e.messages
                })
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
        
@login_required
def signout(request):
    logout(request)
    return redirect('home')


#------------- Gestionar productos (SuperUser) -------------#

@login_required
@user_passes_test(is_superuser)
def Crear_Producto(request):
    if request.method == 'GET':
        return render(request, 'myapp/Crear_Productos.html', {
            'form': ProductoForm()
        })
    else:
        try:
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                nuevo_Producto = form.save(commit=False)
                nuevo_Producto.user = request.user
                nuevo_Producto.save()
                return redirect('lista_Productos')  
            else:
                return render(request, 'myapp/Crear_Productos.html', {
                    'form': form,
                    'error': 'Por favor proporciona datos válidos'
                })
        except Exception as e:
            return render(request, 'myapp/Crear_Productos.html', {
                'form': ProductoForm(),
                'error': f'Ocurrió un error: {str(e)}'
            })

@login_required
@user_passes_test(is_superuser)
def Productos(request):
    Productos = Producto.objects.all()
    return render(request,'myapp/Productos.html',{'Productos': Productos})



@login_required
@user_passes_test(is_superuser)
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
            return redirect('lista_Productos')
        except ValueError:
            return render(request, 'myapp/detalle_Producto.html',
                           {'producto':producto,
                           'form':form,
                            'error': ' Error al actualizar producto'
                            })

@login_required
@user_passes_test(is_superuser)
def eliminar_Producto (request, id_Producto):
    productos = get_object_or_404(Producto, pk=id_Producto)
    if request.method == 'POST':
        productos.delete()
        return redirect('lista_Productos')




#------------- Carrito de compras --------------------#
@login_required
def get_or_create_Carrito(request):
    if request.user.is_authenticated:
        carr, _ = Carrito.objects.get_or_create(user=request.user)
    else:
        carr_id = request.session.get('carr_id')
        if carr_id:
            carr = Carrito.objects.get(id=carr_id)
        else:
            carr = Carrito.objects.create()
            request.session['carr_id'] = carr.id
    return carr

@login_required
def carro_de_compras(request):
    carr = get_or_create_Carrito(request)
    items = producto_item.objects.filter(carr=carr)
    total = sum(item.total for item in items)
    return render(request, 'myapp/carro_de_compras.html', {'items':items, 'total':total})

@login_required
def agregar_al_carrito(request, product_id):
    carr = get_or_create_Carrito(request)
    product = get_object_or_404(Producto, id=product_id)
    carr_item, created = producto_item.objects.get_or_create(carr=carr, product=product)
    
    if not created:
        carr_item.cantidad_item += 1
        carr_item.save()
    
    return redirect('carro_de_compras')

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(producto_item, id=item_id)
    item.delete()
    return redirect('carro_de_compras')

@login_required
def actualiza_carrito(request, item_id):
    item = get_object_or_404(producto_item, id=item_id)
    item.cantidad_item = int(request.POST.get('cantidad_item', 1))
    item.save()
    return redirect('carro_de_compras')


def lista_Productos(request):
        products = Producto.objects.all()
        return render(request, 'myapp/lista_Productos.html',{'products':products})

@login_required
def proceso_de_compras(request):
    return render(request, 'myapp/proceso_de_compras.html')