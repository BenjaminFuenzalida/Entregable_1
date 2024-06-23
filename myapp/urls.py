from django.urls import path
from .views import carro_de_compras, contacto, home, login, pagina_en_mantencion, proceso_de_compras, sign_in
from myapp import views

urlpatterns = [
    path('',home , name='home'),
    path('login/', login, name='login'),
    path('contacto/', contacto, name='contacto'),
    path('carro_de_compras/', carro_de_compras, name='carro_de_compras'),
    path('pagina_en_mantencion/', pagina_en_mantencion, name='pagina_en_mantencion'),
    path('proceso_de_compras/', proceso_de_compras, name='proceso_de_compras'),
    path('sign_in/', sign_in, name='sign_in'),
    
]