from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'core/index.html')

def shop(request):
    productos = Producto.objects.all()
    data ={
        'listaproductos':productos
    }
    return render(request, 'core/shop.html', data)

def base(request):
    return render(request, 'core/base.html')

def detail(request,id):
    producto = Producto.objects.get(id=id) # BUSCA PRODUCTO POR ID
    data={
        'producto' : producto
    }
    return render(request, 'core/detail.html', data)

def contact(request):
    return render(request, 'core/contact.html')
def checkout(request):
    return render(request, 'core/checkout.html')
def cart(request):
    return render(request, 'core/cart.html')
def a(request):
    productos = Producto.objects.all()
    data ={
        'listaproductos':productos
    }
    return render(request, 'core/a.html', data)

def profile(request):
    return render(request, 'core/profile.html')
def comprobante(request):
    return render(request, 'core/comprobante.html')
def informeVenta(request):
    return render(request, 'core/informeVenta.html')
def informeDesempenno(request):
    return render(request, 'core/informeDesempenno.html')
def modificarPerfil(request):
    return render(request, 'core/modificarPerfil.html')
# CRUD PRODUCTO

import requests #libréría para hacer llamadas REST

def shoptest(request):
    data = {}
    try:
        response = requests.get("http://127.0.0.1:5000/listado/")
        if response.status_code in (200, 201):
            data['productos'] = response.json() 
        else:
            data['error'] = "Error al obtener los productos Otro: " + response.text
    except requests.exceptions.RequestException as e:
        data['error'] = f"Error al conectar con la API: {e}"

    return render(request, 'core/shoptest.html', data)


def addProduct(request):
    data={
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) # RECIBE TODA INFO DEL FORM
        if formulario.is_valid():
            json = {
                "nombre": formulario['nombre'],
                "imagen": formulario['imagen'],
                "tipo_id": formulario['tipo_id'],
                "precio": formulario['precio'],
                "stock": formulario['stock'],
            }
            try:
                response = requests.post("http://127.0.0.1:5000/addProduct/",json)
                if response.status_code == 201:
                    formulario.save()
                    data['msj'] = "Producto agregado correctamente!"
                else:
                    data['msj'] = "Error al agregar el producto: " + response.text
            except requests.exceptions.RequestException as e:
                data['msj'] = f"Error al conectar con la API: {e}"
    return render(request, 'core/addProduct.html', data)


def updateProduct(request,id):
    producto = Producto.objects.get(id=id) # BUSCA PRODUCTO POR ID
    data={
        'producto' : producto,
        'form': ProductoForm(instance=producto) # CARGA INFO EN EL FORM
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance = producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['form'] = formulario
            data['msj'] = "Producto modificado correctamente!"
    return render(request, 'core/updateProduct.html',data)

def deleteProduct(request,id):
    producto= Producto.objects.get(id=id)# BUSCA PRODUCTO POR ID
    producto.delete()
    return redirect(to="shop")
