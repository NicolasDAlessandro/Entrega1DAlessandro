from django.urls import path 
from . import views
urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('nuevo_vendedor/', views.nuevo_vendedor, name="nuevoVendedor"),
    path('nuevo_cliente/', views.nuevo_cliente, name="nuevoCliente"),
    path('nuevo_producto/', views.nuevo_producto, name="nuevoProducto"),
    path('buscar_cliente/', views.buscarCliente, name="buscarCliente"),
    path('buscar_vendedor/', views.buscarVendedor, name="buscarVendedor"),
    path('buscar_producto', views.buscarProducto, name="buscarProducto")
]
