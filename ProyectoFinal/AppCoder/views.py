from django.shortcuts import render
from django.shortcuts import redirect, render
from . import models 


def inicio_view(request):
    return render(request, "AppCoder/inicio.html")

def productos_view(request):
    return render(request, "AppCoder/productos.html") 

def wish_view (request):
    Solicitados = models.Producto.objects.all()
    context = {"producto": Solicitados}
    return render(request, "AppCoder/wish.html", context)

def clientes_view(request):
    Clientes = models.Cliente.objects.all()
    context = {"clientes": Clientes}
    return render(request, "AppCoder/clientes.html", context) 

from . import forms

def crear_view(request): 
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("AppCoder:clientes")
    else:
        form = forms.ClienteForm()
    return render(request, "AppCoder/crear.html", {"form": form})

def productos_solicitados_view(request): 
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("AppCoder:wish")
    else:
        form = forms.ProductoForm() 
    return render(request, "AppCoder/solicitados.html", {"form": form})  
