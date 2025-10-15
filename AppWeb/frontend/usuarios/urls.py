from django.urls import path
from .views import lista_usuarios, crear_usuario, actualizar_usuario, eliminar_usuario

urlpatterns = [
    path('', lista_usuarios, name='lista_usuarios'),
    path('crear/', crear_usuario, name='crear_usuario'),
    path('actualizar/<int:id>/', actualizar_usuario, name='actualizar_usuario'),
    path('eliminar/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
]