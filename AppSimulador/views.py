from math import prod
from urllib.request import Request
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.shortcuts import render,redirect
from .forms import formVendedor,formCliente,formProducto
from .models import Vendedor,Cliente,Producto


def inicio(request):
    return render(request,"inicio.html")

def nuevo_vendedor(request):
    if request.method == "POST":
        formulario = formVendedor(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            vendedor = Vendedor(nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                legajo = informacion["legajo"])
            vendedor.save()
            return redirect("Inicio")
    formulario = formVendedor()
    return render(request,"formVendedor.html",{"form": formulario})

def nuevo_cliente(request):
    if request.method == "POST":
        formulario = formCliente(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cliente = Cliente(nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                dni = informacion["dni"],
                tipoFacturacion = informacion["tipoFacturacion"])
            cliente.save()
            return redirect("Inicio")
    formulario = formCliente()
    return render(request,"formCliente.html",{"form":formulario})

def nuevo_producto(request):
    if request.method == "POST":
        formulario = formProducto(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            prod = Producto(nombre = informacion["nombre"],
                precio = informacion["precio"],
                stock = informacion["stock"])
            prod.save()
            return redirect("Inicio")
    formulario = formProducto()
    return render(request,"formProducto.html",{"form":formulario})

def buscarCliente (request):
    if request.GET.get("dni"):
        dni = request.GET.get("dni")
        busquedas = Cliente.objects.filter(dni__icontains=dni)
        return render(request,'resultadoBusqueda.html', {"busquedas":busquedas})
    return render(request,"busquedaCliente.html")

def buscarVendedor(request):
    if request.GET.get("legajo"):
        legajo = request.GET.get("legajo")
        busquedas = Vendedor.objects.filter(legajo__icontains=legajo)
        return render (request,"resultadoBusqueda.html",{"busquedas":busquedas})
    return render(request,"busquedaVendedor.html")

def buscarProducto(request):
    if request.GET.get("nombre"):
        nombre = request.GET.get("nombre")
        busquedas = Producto.objects.filter(nombre__icontains=nombre)
        return render (request,"resultadoBusqueda.html",{"busquedas":busquedas})
    return render(request,"busquedaProducto.html")