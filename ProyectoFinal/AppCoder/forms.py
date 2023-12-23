from django import forms

from .import models
from .models import Blog

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["nombre", "apellido"]
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["autor", "titulo", "imagen", "descripcion"]


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["nombre_producto"]

class stock_busqueda (forms.Form):
      stock = forms.CharField()


from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel

class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["password1", "password2", "username", "email"]
        help_texts = {k: "" for k in fields}

class UserEditionFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}

from .models import Avatar     
class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["imagen"]