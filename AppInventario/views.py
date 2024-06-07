from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from .models import UnidadMedida, TipoEquipo, TipoProducto
from .forms import UnidadMedidaForm, TipoEquipoForm, TipoProductoForm

def login_web(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                return render(request, "AppInventario/base.html")
    else:
        form = AuthenticationForm()
    return render(request, "AppInventario/login.html", {"form":form})


def unidades_de_medida(request):
    unidades = UnidadMedida.objects.all()
    form = UnidadMedidaForm()
    editing = False
    id = None
    if request.method == "POST":
        if "Agregar" in request.POST:
            form = UnidadMedidaForm(request.POST)
            if form.is_valid():
                form.save()
                form = UnidadMedidaForm()
                return redirect('unidadesmedidas')
        elif "Editar" in request.POST:
            seleccion = UnidadMedida.objects.get(id=request.POST.get("id"))
            form = UnidadMedidaForm(instance=seleccion)
            editing = True
            id = post.id
    return render(request, "AppInventario/unidad_medida.html",{"unidades":unidades,})

def index(request):
    return render(request, "AppInventario/base.html")


def tipo_de_producto(request):
    tipo_de_producto = TipoProducto.objects.all()
    unidades = UnidadMedida.objects.all()
    form = TipoProductoForm()
    if request.method == "POST":
        if "agregar" in request.POST:
            form = TipoProductoForm(request.POST)
            if form.is_valid():
                form.save()
                form = TipoProductoForm()
                return redirect('tipo_de_producto')

    return render(request, "AppInventario/tipo_de_producto.html", {
        "tipo_de_producto": tipo_de_producto,
        "unidades" : unidades,
        "form": form
    })

  
def modulo_tipo_equipo(request):
    tipos_de_equipo = TipoEquipo.objects.all()
    form = TipoEquipoForm()

    if request.method == "POST":
        if "agregar" in request.POST:
            form = TipoEquipoForm(request.POST)
            if form.is_valid():
                form.save()
                form = TipoEquipoForm()
                return redirect('modulotipoequipo')

    return render(
        request, 
        "AppInventario/modulo_tipo_equipo.html", 
        {
            "tipos_de_equipo": tipos_de_equipo,
            "form": form,
        },
    )
