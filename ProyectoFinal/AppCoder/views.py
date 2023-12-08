
from django.shortcuts import redirect, render
from . import models 
from . import forms
from .forms import stock_busqueda
from .models import stock

def inicio_view(request):
    return render(request, "AppCoder/inicio.html")


def buscar_view(request):
   if request.method == "GET": 
       form = stock_busqueda() 
       return render(request, "AppCoder/buscar.html", {"form": form})
   else:
       formulario = forms.stock_busqueda(request.POST)
       if formulario.is_valid():
            informacion = formulario.cleaned_data
            filtrados = []
            for stock in models.stock.objects.filter (stock =informacion["stock"]):
                filtrados.append(stock)
            
            contexto = {"stock": filtrados}
            return render(request, "AppCoder/stock.html", contexto)

def productos_view(request):    
    Stock= models.stock.objects.all() 
    context = {"stock": Stock}
    return render(request, "AppCoder/productos.html",context) 

def wish_view (request):
    Solicitados = models.Producto.objects.all()
    context = {"producto": Solicitados}
    return render(request, "AppCoder/wish.html", context)

def clientes_view(request):
    Clientes = models.Cliente.objects.all()
    context = {"clientes": Clientes}
    return render(request, "AppCoder/clientes.html", context) 


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
