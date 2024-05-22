from django.urls import path
from .views import *

urlpatterns = [
        path('', index, name="index"),
        path('shop/', shop, name="shop"),
        path('shoptest/', shoptest, name="shoptest"),
        path('base/', base, name="base"),
        path('detail/<id>/', detail, name="detail"),
        path('contact/', contact, name="contact"),
        path('checkout/', checkout, name="checkout"),
        path('cart/', cart, name="cart"),
        path('a', a, name="a"),
        path('profile/', profile, name="profile"),
        path('comprobante/', comprobante, name="comprobante"),
        path('informeVenta/', informeVenta, name="informeVenta"),
        path('informeDesempenno/', informeDesempenno, name="informeDesempenno"),
        path('modificarPerfil/', modificarPerfil, name="modificarPerfil"),

        # CRUD PRODUCTO
        path('addProduct/', addProduct, name="addProduct"),
        path('updateProduct/<id>/', updateProduct, name="updateProduct"),
        path('deleteProduct/<id>/', deleteProduct, name="deleteProduct"),
        
]