from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "AppInventario/base.html")

def tipo_de_producto(request):
    return render(request, 'AppInventario/tipo_de_producto.html')