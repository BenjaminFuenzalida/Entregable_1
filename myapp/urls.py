from django.urls import path
from .views import carro_de_compras, contacto, home, login, pagina_en_mantencion, proceso_de_compras, sign_up
from . import views

urlpatterns = [
    path('',home , name='home'),
    path('contacto/', contacto, name='contacto'),
    path('carro_de_compras/', carro_de_compras, name='carro_de_compras'),
    path('pagina_en_mantencion/', pagina_en_mantencion, name='pagina_en_mantencion'),
    path('proceso_de_compras/', proceso_de_compras, name='proceso_de_compras'),

    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('logout/', views.signout, name='lougout'),

    path('Productos/', views.Productos, name='Productos'),
    path('Productos/Crear/', views.Crear_Producto, name='Crear_Producto'),
    path('Productos/<int:id_Producto>/', views.detalle_Producto, name='detalle_Producto'),
    path('Productos/<int:id_Producto>/Producto_completado', views.Producto_completado, name='Producto_completado'),


]
