from django.urls import path
from AppCoder.views import (
    
    inicio_view,
    productos_view,
    # productos_buscar_view,
    clientes_view,
    crear_view,
    wish_view,
    productos_solicitados_view,
    
    )

app_name = "AppCoder"

urlpatterns = [
    path("", inicio_view, name="inicio"),
    # path("productos/buscar/", productos_buscar_view, name= "productos_buscar"),
    path("productos/", productos_view, name="productos"),
    path("wish/", wish_view, name="wish"),
    path("wish/crear", productos_solicitados_view, name="solicitados"),
    path("clientes/", clientes_view, name="clientes"),
    path("clientes/crear", crear_view, name= "crear"),
    
]