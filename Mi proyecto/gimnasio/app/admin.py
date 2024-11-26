from django.contrib import admin
from .models import Plan, Contacto
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email')
    

class planAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio')

class contactoadmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email','tipo_consulta', 'mensaje')

admin.site.register(Plan, planAdmin)

admin.site.register(Contacto, contactoadmin)

admin.site.register(Usuario)



