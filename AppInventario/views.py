from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from .models import TipoProducto, UnidadMedida
from .forms import TipoProductoForm

def login_web(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        #print(form)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            #print(user)
            if user is not None:
                login(request, user)
                return render(request, "AppInventario/base.html")
    else:
        form = AuthenticationForm()
    return render(request, "AppInventario/login.html", {"form":form})

def index(request):
    return render(request, "AppInventario/base.html")

def tipo_de_producto(request):
    tipo_de_producto = TipoProducto.objects.all()
    unidades = UnidadMedida.objects.all()
    print(tipo_de_producto[0].unidad_medida)
    form = TipoProductoForm()
    if request.method == "POST":
        if "agregar" in request.POST:
            form = TipoProductoForm(request.POST)
            if form.is_valid():
                form.save()
                form = TipoProductoForm()

    return render(request, "AppInventario/tipo_de_producto.html", {
        "tipo_de_producto": tipo_de_producto,
        "unidades" : unidades,
        "form": form
    })