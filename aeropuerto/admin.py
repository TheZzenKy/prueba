from django.contrib import admin
from .models import Pasajero, Billete, Piloto, Aeropuerto, Vuelo, Avion, Fabricante, Aerolinea
# Register your models here.

@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "rut", "telefono", "nacionalidad",)

@admin.register(Billete)
class BilleteAdmin(admin.ModelAdmin):
    list_display = ("origen", "destino", "asiento", "fecha_ida", "fecha_vuelta",)

@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = ("nombre_piloto", "apellido_piloto", "rut", "telefono",)

@admin.register(Aeropuerto)
class AeropuertoAdmin(admin.ModelAdmin):
    list_display = ("nombre_aeropuerto", "ubicacion",)

@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ("codigo_vuelo", "fecha_salida", "fecha_llegada",)

@admin.register(Avion)
class AvionAdmin(admin.ModelAdmin):
    list_display = ("matricula", "modelo", "activo",)

@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ("sucursal", "telefono", "email",)

@admin.register(Aerolinea)
class AerolineaAdmin(admin.ModelAdmin):
    list_display = ("nombre_aerolinea",)