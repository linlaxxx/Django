from django.contrib import admin

from .models import Cliente, Reparacion

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'direccion')
    search_fields = ('nombre', 'telefono', 'correo')

class ReparacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_recepcion', 'fecha_entrega', 'estatus')
    list_filter = ('estatus', 'fecha_recepcion')
    search_fields = ('cliente__nombre', 'detalles_equipo', 'descripcion_equipo')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Reparacion, ReparacionAdmin)

