from django.contrib import admin
from .models import*

#class ProductoAdmin(admin.ModelAdmin):
#    list_display = ['nombre','precio','tipo_id','stock','imagen']
#    search_fields = ['nombre']
#    list_per_page: 10
#    list_filter = ['tipo_id']
#    list_editable = ['tipo_id','precio','imagen','stock']

# Register your models here.
admin.site.register(TipoEmpleado)
admin.site.register(TipoProducto)
admin.site.register(Empleado)
admin.site.register(Cliente)
#admin.site.register(Producto, ProductoAdmin)
admin.site.register(Boleta)
admin.site.register(DetalleBol)
admin.site.register(Envio)
