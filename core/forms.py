from django import forms
from django.forms import ModelForm
from .models import *

class ProductoForm (ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class TipoProductoForm (ModelForm):
    class Meta:
        model = TipoProducto
        fields = '__all__'