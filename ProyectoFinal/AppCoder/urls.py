from django.urls import path
from. import views
from django.contrib.auth.views import LogoutView
from AppCoder.views import (
    
    inicio_view,
    historia_view,
    productos_view,
    wish_view,
    productos_solicitados_view,
    clientes_view,
    crea_socio,
    registro_view,
    login_view,
    logout_view,
    editar_perfil_view,
    
    crear_avatar_view,
    
    delete_view,
    editar_socio,
    crea_blog_view, 
    visualizar_blogs_view,
  

   
    
    
    )

app_name = "AppCoder"

urlpatterns = [
    path("", inicio_view, name="inicio"),
    path("historia/", historia_view, name="historia"),
    path("productos/", productos_view, name="productos"),
    path("wish/", wish_view, name="wish"),
    path("wish/crear", productos_solicitados_view, name="solicitados"),
    path("clientes/", clientes_view, name="socios"),
    path("crear-socio/", crea_socio, name="crea-socio"),
    path("registro/", registro_view, name="registro"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("editar-perfil/", editar_perfil_view, name="editar-perfil"),
    path("crear-avatar/", crear_avatar_view, name="crear-avatar"), # type: ignore
    path("delete/<int:pk>", delete_view, name="delete"), # type: ignore
    path("editar/<int:pk>",  editar_socio, name="editar"),
    path('crear-blog/', crea_blog_view, name='crear-blog'),
    path('visualizar-blogs/', visualizar_blogs_view, name='visualizar-blogs'),
    
    ]