from django.contrib import admin
from django.forms import Field
from .models import Proyecto

# Register your models here.
class ProyectoAdministrador(admin.ModelAdmin):
    readonly_fields = ('enlace', 'creado', 'modificado')


admin.site.register(Proyecto, ProyectoAdministrador)
