from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from .models import TipoEquipo, TipoProducto
from .forms import TipoEquipoForm

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
    form = TipoEquipoForm()

    if request.method == "POST":
        print(request.POST)
        if "agregar" in request.POST:
            form = TipoEquipoForm(request.POST)
            if form.is_valid():
                form.save()
                form = TipoEquipoForm()


    return render(
        request, 
        "AppInventario/modulo_tipo_equipo.html", 
        {
            "tipos_de_equipo": tipos_de_equipo,
            "form": form,
        },
    )