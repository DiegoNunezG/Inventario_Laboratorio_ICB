from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from .models import (
    UnidadMedida, 
    TipoEquipo, 
    TipoProducto, 
    Marca, 
    Equipo, 
    Producto, 
    OrdenIngreso, 
    DetalleIngreso
    )
from .forms import (
    UnidadMedidaForm, 
    TipoEquipoForm, 
    TipoProductoForm, 
    MarcaForm, 
    EquipoForm, 
    ProductoForm, 
    OrdenIngresoForm, 
    ProductoFormSet
    )
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.views.generic import TemplateView, ListView

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
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login') # Redirige a la página de inicio de sesión después de cerrar sesión


@login_required(login_url='login')
def unidades_de_medida(request):
    unidades = UnidadMedida.objects.all()
    form = UnidadMedidaForm()
    editing = False
    id_ = None

    if request.method == "POST":
        if "agregar" in request.POST:
            form = UnidadMedidaForm(request.POST)
            if "editing" in request.POST:
                form = UnidadMedidaForm(request.POST, instance=UnidadMedida.objects.get(id=request.POST.get("id")))
            if form.is_valid():
                if "editing" in request.POST:
                    selection = UnidadMedida.objects.get(id=request.POST.get("id"))
                    selection.nombre = form.cleaned_data["nombre"]
                    selection.simbolo = form.cleaned_data["simbolo"]
                    selection.save()
                    editing = False
                    form = UnidadMedida()
                else:
                    form.save()
                    form = UnidadMedida()
            return redirect('unidadesmedidas')
        
        elif "editar" in request.POST:
            selection = UnidadMedida.objects.get(id=request.POST.get("id"))
            data = {'id': selection.id, 'nombre': selection.nombre, 'simbolo': selection.simbolo}
            form = UnidadMedidaForm(initial=data)
            editing = True
            id_ = selection.id

    return render(request, "AppInventario/unidad_medida.html",{
        "unidades":unidades,
        "form": form,
        "editing": editing,
        "id": id_,})

@login_required(login_url='login')
def index(request):
    return render(request, "AppInventario/base.html")


@login_required(login_url='login')
def tipo_de_producto(request):
    tipo_de_producto = TipoProducto.objects.all()
    unidades = UnidadMedida.objects.all()
    form = TipoProductoForm()
    editing = False
    id = None
    if request.method == "POST":
        if "agregar" in request.POST:
            form = TipoProductoForm(request.POST)
            if "editing" in request.POST:
                print(request.POST)
                form = TipoProductoForm(request.POST, instance=TipoProducto.objects.get(id=request.POST.get("id")))
            if form.is_valid():
                if "editing" in request.POST:
                    seleccion = TipoProducto.objects.get(id=request.POST.get("id"))
                    seleccion.nombre = form.cleaned_data["nombre"]
                    seleccion.unidad_medida = form.cleaned_data["unidad_medida"]
                    seleccion.save()
                    editing = False
                    id = None
                else:
                    form.save()
                    form = TipoProductoForm()
            return redirect('tipo_de_producto')
        elif "Editar" in request.POST:
            seleccion = TipoProducto.objects.get(id=request.POST.get("id"))
            form = TipoProductoForm(instance=seleccion)
            editing = True
            id = seleccion.id            
         
    return render(request, "AppInventario/tipo_de_producto.html",{"tipo_de_producto":tipo_de_producto, "editing": editing, "id" : id, "form": form})

  
@login_required(login_url='login')
def modulo_tipo_equipo(request):
    tipos_de_equipo = TipoEquipo.objects.all()
    form = TipoEquipoForm()
    editing = False

    if request.method == "POST":
        if "agregar" in request.POST:
            form = TipoEquipoForm(request.POST)
            if "editing" in request.POST:
                form = TipoEquipoForm(request.POST, instance=TipoEquipo.objects.get(id=request.POST.get("id")))
            if form.is_valid():
                if "editing" in request.POST:
                    selection = TipoEquipo.objects.get(id=request.POST.get("id"))
                    selection.nombre = form.cleaned_data["nombre"]
                    selection.tipo_producto.set(form.cleaned_data["tipo_producto"])
                    selection.save()
                    editing = False
                    form = TipoEquipoForm()
                else:
                    form.save()
                    form = TipoEquipoForm()
                return redirect('modulotipoequipo')
            else:
                print(form.errors)

        if "editar" in request.POST:
            selection = TipoEquipo.objects.get(id=request.POST.get("id"))
            data = {'id':selection.id, 'nombre':selection.nombre, "tipo_producto":selection.tipo_producto.all()}
            form = TipoEquipoForm(initial=data)
            editing = True
            id_ = selection.id
            return render(request, "AppInventario/modulo_tipo_equipo.html", {"form":form, "tipos_de_equipo": tipos_de_equipo, "editing":editing, "id":id_})

    return render(
        request, 
        "AppInventario/modulo_tipo_equipo.html", 
        {
            "tipos_de_equipo": tipos_de_equipo,
            "form": form,
            "editing": editing,
        },
    )
 

@login_required(login_url='login')
def marca_de_producto(request):
    marcas = Marca.objects.all()
    form = MarcaForm()
    editing = False
    id = None
    if request.method == "POST":
        #print(request.POST)
        if "Agregar" in request.POST:
            form = MarcaForm(request.POST)
            if "editing" in request.POST:
                form = MarcaForm(request.POST, instance=Marca.objects.get(id=request.POST.get("id")))
            if form.is_valid():
                if "editing" in request.POST:
                    seleccion = Marca.objects.get(id=request.POST.get("id"))
                    seleccion.nombre = form.cleaned_data["nombre"]
                    seleccion.save()
                    editing = False
                    id = None
                else:
                    form.save()
                    form = MarcaForm()
            return redirect('marcadeproducto')
        elif "Editar" in request.POST:
            seleccion = Marca.objects.get(id=request.POST.get("id"))
            form = MarcaForm(instance=seleccion)
            editing = True
            id = seleccion.id
    return render(request, "AppInventario/marca_de_producto.html",{"marcas":marcas, "editing": editing, "id" : id, "form": form})

  
@login_required(login_url='login')
def equipo(request):
    equipo =   Equipo.objects.all()
    tipo_equipo = TipoEquipo.objects.all()
    form = EquipoForm()
    editing = False
    deleting = False
    id_ = None

    if request.method == "POST":
        print(request.POST)

        if "agregar" in request.POST:
            form = EquipoForm(request.POST)
            if "editing" in request.POST:
                form = EquipoForm(request.POST, instance=Equipo.objects.get(id=request.POST.get("id")))
            if form.is_valid():
                if "editing" in request.POST:
                    selection = Equipo.objects.get(id=request.POST.get("id"))
                    selection.nombre = form.cleaned_data["nombre"]
                    selection.tipo_equipo = form.cleaned_data["tipo_equipo"]
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
            selection = Equipo.objects.get(id=request.POST.get("id"))
            id_ = selection.id
            deleting = True
        
        elif "deleting" in request.POST:
            deleting = False
            id_ = None
            if "cancelar_delete" in request.POST:
                print()
                return redirect('equipo')
            elif "confirmar_delete" in request.POST: 
                Equipo.objects.get(id=request.POST.get("id")).delete()
                return redirect('equipo')


    return render(request, "AppInventario/modulo_equipo.html", {
        "tipo_equipo": tipo_equipo,
        "equipo" : equipo,
        "form": form,
        "editing": editing,
        "deleting": deleting,
        "id": id_,
        "form": form,
    })


@login_required(login_url='login')
def producto(request):
    producto = Producto.objects.all()
    tipo_producto = TipoProducto.objects.all()
    form = ProductoForm()
    editing = False
    id = None
    return render(request, "AppInventario/modulo_producto.html", {
        "productos": producto,
        "tipo_producto": tipo_producto,
        "form": form,
    })


@login_required(login_url='login')
def orden_ingreso(request):
    ordenes = OrdenIngreso.objects.all()
    detalles = DetalleIngreso.objects.all()
    form = OrdenIngresoForm()

    return render(request, "AppInventario/orden_ingreso.html", {
        "ordenes": ordenes,
        "detalles": detalles,
        "form": form,
    })


@login_required(login_url='login')
def interfaz_ingreso(request):
    producto_form = ProductoForm()
    orden_form = OrdenIngresoForm()

    context = {
        'producto_form': producto_form,
        'orden_form': orden_form 
    }

    if request.method == "POST":
        producto_form = ProductoForm(request.POST)
        orden_form = OrdenIngresoForm(request.POST)
        if producto_form.is_valid() and orden_form.is_valid():
            try:
                cantidad = int(request.POST.get('cantidad'))
            except:
                print("ERROR")

            ord = orden_form.save()
            for i in range(cantidad):
                pcto = ProductoForm(request.POST)
                pcto = pcto.save()
            detalle_ingreso = DetalleIngreso(orden=ord, producto=pcto, cantidad=cantidad)
            detalle_ingreso.save()
            return redirect(reverse_lazy("orden_ingreso"))
    return render(request, "AppInventario/interfaz_ingreso.html", context)


# Esta clase no se usa por ahora. En el futuro servirá para ingresar multiples productos a la vez
class AddOrden(TemplateView):
    template_name="AppInventario/interfaz_ingreso.html"

    def get(self, *args, **kargs):
        formset = ProductoFormSet(queryset=Producto.objects.none())
        print(formset)
        return self.render_to_response({'producto_formset': formset})
    
    def post(self, *args, **kargs):
        formset = ProductoFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("orden_ingreso"))
        
        return self.render_to_response({'producto_formset': formset})
        