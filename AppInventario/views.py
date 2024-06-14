from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from .models import UnidadMedida, TipoEquipo, TipoProducto, Equipo, Producto
from .forms import UnidadMedidaForm, TipoEquipoForm, TipoProductoForm, EquipoForm

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


def equipo(request):
    equipo =   Equipo.objects.all()
    tipo_equipo = TipoEquipo.objects.all()
    form = EquipoForm()
    editing = False
    id_ = None

    if request.method == "POST":
        if "agregar" in request.POST:
            form = EquipoForm(request.POST)
            if "editing" in request.POST:
                form = EquipoForm(request.POST, instance=Equipo.objects.get(id=request.POST.get("id")))
            if form.is_valid():
                if "editing" in request.POST:
                    selection = Equipo.objects.get(id=request.POST.get("id"))
                    selection.nombre = form.cleaned_data["nombre"]
                    selection.tipo_producto = form.cleaned_data["tipo_equipo"]
                    selection.productos.set(form.cleaned_data["productos"])
                    selection.save()
                    editing = False
                    form = EquipoForm()
                else:
                    form.save()
                    form = EquipoForm()
            return redirect('equipo')
        
        elif "editar" in request.POST:
            selection = Equipo.objects.get(id=request.POST.get("id"))
            data = {'id': selection.id, 'nombre': selection.nombre, 'tipo_equipo': selection.tipo_equipo, 'productos': selection.productos.all()}
            form = EquipoForm(initial=data)
            editing = True
            id_ = selection.id

        elif "eliminar" in request.POST:
            Equipo.objects.get(id=request.POST.get("id")).delete()
            return redirect('equipo')

    return render(request, "AppInventario/modulo_equipo.html", {
        "tipo_equipo": tipo_equipo,
        "equipo" : equipo,
        "form": form,
        "editing": editing,
        "id": id_,
    })