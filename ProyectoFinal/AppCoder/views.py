from django.shortcuts import render
from django.shortcuts import redirect, render



def inicio_view(request):
    return render(request, "AppCoder/inicio.html")

def productos_view(request):
    return render(request, "AppCoder/productos.html") 