from django.urls import path
from AppCoder.views import (
    
    inicio_view,
    productos_view,
    
    )

app_name = "AppCoder"

urlpatterns = [
    path("", inicio_view, name="inicio"),
    path("productos/", productos_view, name="productos"),
]