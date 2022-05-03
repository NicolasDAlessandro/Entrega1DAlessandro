from django import forms

class formVendedor(forms.Form):

    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    legajo = forms.IntegerField()

class formCliente(forms.Form):

    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    dni = forms.IntegerField()
    tipoFacturacion = forms.CharField(max_length=100)


class formProducto(forms.Form):

    nombre = forms.CharField(max_length=100)
    precio = forms.IntegerField()   
    stock = forms.IntegerField() 