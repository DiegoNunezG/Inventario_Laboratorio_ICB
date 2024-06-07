from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from .models import TipoEquipo, TipoProducto

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


def modulo_tipo_equipo(request):
    tipos_de_equipo = TipoEquipo.objects.all()

    # tipos_de_producto = {}
    # for tipo_de_equipo in tipos_de_equipo:
    #     tipos_de_producto[f"{tipo_de_equipo.nombre}"] = tipo_de_equipo.tipoproducto_set.all()
    # print(tipos_de_producto[tipos_de_equipo[0].nombre])
    for item in tipos_de_equipo[0].tipo_producto.all():
        print(item)
    
    
    return render(
        request, 
        "AppInventario/modulo_tipo_equipo.html", 
        {
            "tipos_de_equipo": tipos_de_equipo,
        },
    )