from django.urls import path
from .views import home, contacto, planes, agregar_plan, listar_planes, modificar_plan, eliminar_plan, informacion, iniciar_sesion, registro_usuario

urlpatterns = [
    path('',home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('planes/', planes, name='planes'),
    path('agregar_plan/', agregar_plan, name='agregar_plan'),
    path('listar_planes/', listar_planes, name='listar_planes'),
    path('modificar_plan/<id>/', modificar_plan, name='modificar_plan'),
    path('eliminar_plan/<id>/', eliminar_plan, name='eliminar_plan'),
    path('informacion/', informacion, name='informacion'),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registro_usuario/', registro_usuario, name='registro_usuario'),
]