from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def login(request):
    return render(request, 'myapp/login.html')

def contacto(request):
    return render(request, 'myapp/contacto.html')

def carro_de_compras(request):
    return render(request, 'myapp/carro_de_compras.html')

def pagina_en_mantencion(request):
    return render(request, 'myapp/pagina_en_mantencion.html')

def proceso_de_compras(request):
    return render(request, 'myapp/proceso_de_compras.html')

def sign_in(request):
    return render(request, 'myapp/sign_in.html')


