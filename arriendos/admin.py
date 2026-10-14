from django.contrib import admin
from arriendos.models import Equipo, Arriendo

# Register your models here.
class EquipoVista(admin.ModelAdmin):
    list_display = ["nombre", "arrendado", "valor", "fecha_ingresado"]
    search_fields = ["fecha_ingresado", "nombre"]

admin.site.register(Equipo, EquipoVista)
admin.site.register(Arriendo)