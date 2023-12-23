
from django.shortcuts import redirect, render
from . import models 
from . import forms

from .models import stock, Avatar, Cliente

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def inicio_view(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        
        avatar_url = ""

    return render(request, "AppCoder/inicio.html", context={"avatar_url": avatar_url})


def historia_view(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        
        avatar_url = ""

    return render(request, "AppCoder/about.html", context={"avatar_url": avatar_url})


def productos_view(request):    
    Stock= models.stock.objects.all() 
    context = {"stock": Stock}
    return render(request, "AppCoder/productos.html",context) 

@login_required
def wish_view (request):
    Solicitados = models.Producto.objects.all()
    context = {"producto": Solicitados}
    return render(request, "AppCoder/wish.html", context)

def clientes_view(request):
    Clientes = models.Cliente.objects.all()
    context = {"clientes": Clientes}
    return render(request, "AppCoder/clientes.html", context) 



@login_required
def productos_solicitados_view(request): 
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("AppCoder:wish")
    else:
        form = forms.ProductoForm() 
    return render(request, "AppCoder/solicitados.html", {"form": form})  

from .forms import UserCreationFormulario, UserEditionFormulario, UserAvatarFormulario
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout

def login_view(request):

    if request.user.is_authenticated:
        return render(
            request,
            'AppCoder/autenticado.html',
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )
    if request.method == "GET":
        return render(
            request,
            "AppCoder/login.html",
            {"form": AuthenticationForm()}
        )
   
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(
                request,
                "AppCoder/felicitaciones.html",
                {"mensaje": f" {usuario}"} 
            )
        else:
            return render(
                request,
                "AppCoder/login.html",
                {"form": formulario}
            )
            
def logout_view(request):
    logout(request)
    return redirect("AppCoder:inicio")


from .forms import UserCreationFormulario, UserEditionFormulario, UserAvatarFormulario, ClienteForm
from django.contrib.auth.views import PasswordChangeView


def registro_view(request):

    if request.method == "GET":
        return render(
            request,
            "AppCoder/registro.html",
            {"form": UserCreationFormulario()}
        )
    else:
        formulario = UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "AppCoder/felicitaciones.html",
                {"mensaje": f" Su usuario: {usuario} ya fue creado"}
            )
        else:
            return render(
                request,
                "AppCoder/registro.html",
                {"form": formulario}
            )
def editar_perfil_view(request):

    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).last()
    avatar_url = avatar.imagen.url if avatar is not None else ""

    if request.method == "GET":
        valores_iniciales = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }
        formulario = UserEditionFormulario(initial=valores_iniciales)
        return render(
            request,
            "AppCoder/editar_perfil.html",
            context={"form": formulario, "usuario": usuario,"avatar_url": avatar_url}
            )
    else:
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]

            usuario.set_password(informacion["password1"])

            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
        return redirect("AppCoder:inicio")
    

def crear_avatar_view(request):

    usuario = request.user

    if request.method == "GET":
        formulario = UserAvatarFormulario()
        return render(
            request,
            "AppCoder/crear_avatar.html",
            context={"form": formulario, "usuario": usuario}
        )
    else:
        formulario = UserAvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Avatar(user=usuario, imagen=informacion["imagen"])
            modelo.save()
            return redirect("AppCoder:inicio")
        

 
def crea_socio(req):
    if req.method == "POST":
        miformulario = ClienteForm(req.POST) 
        if miformulario.is_valid():
            data = miformulario.cleaned_data
            cliente = models.Cliente(nombre=data["nombre"],
                  apellido=data["apellido"])  
            cliente.save()
            return redirect ("AppCoder:socios")
        return render (req, "AppCoder/crear.html", {"miformulario" : miformulario})
    else:
        miformulario = ClienteForm() 
        return render (req, "AppCoder/crear.html", {"miformulario" : miformulario}) 

def eliminar_socio(request, id):
    if request.method == "POST":
        clientes = Cliente.objects.filter(id=id)
        clientes.delete()
        clientes = models.Cliente.objects.all()
        return render (request,"AppCoder/clientes.html", {"clientes": clientes})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente

def delete_view(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)

    if request.method == 'POST':
        cliente.delete()
        return redirect('AppCoder:socios')  # Redirigir a la página de clientes después de eliminar

    clientes = Cliente.objects.all()
    return render(request, "AppCoder/clientes.html", {"clientes": clientes})

def editar_socio(req, pk):
    clientes = Cliente.objects.get(id= pk)

    if req.method == "POST":
        miformulario = ClienteForm(req.POST) 

        if miformulario.is_valid():
            data = miformulario.cleaned_data
            
            clientes.nombre = data["nombre"]
            clientes.apellido  = data["apellido"]
            clientes.save()
            return redirect ("AppCoder:socios")
        return render (req, "AppCoder/editarform.html", {"miformulario" : miformulario})
    else:
        
        miformulario = ClienteForm(initial={ "nombre": clientes.nombre, "apellido": clientes.apellido }) 
        return render (req, "AppCoder/editarform.html", {"miformulario" : miformulario, "id": clientes.pk}) 

from django.shortcuts import render, redirect
from .forms import BlogForm

def crea_blog_view(request):
    if request.method == "POST":
        formulario = BlogForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("AppCoder:inicio") 
    else:
        formulario = BlogForm()
    return render(request, "AppCoder/crear_blog.html", {"formulario": formulario})

from django.shortcuts import render
from .models import Blog

def visualizar_blogs_view(request):
    blogs = Blog.objects.all()
    return render(request, "AppCoder/visualizar_blogs.html", {"blogs": blogs})


