from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from AppInventario.views import login_web, index, unidades_de_medida, modulo_tipo_equipo, tipo_de_producto, marca_de_producto, equipo, producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_web, name="login"),
    path('', LogoutView.as_view(), name='logout'), #aqui se puede cambiar el path de logout
    path('index/', index),
    path('unidades-de-medidas/', unidades_de_medida, name='unidadesmedidas'),
    path('tipos-de-equipo/', modulo_tipo_equipo, name='modulotipoequipo'),
    path('tipos-de-producto/', tipo_de_producto, name='tipo_de_producto'),
    path('marcas-de-producto/', marca_de_producto, name='marcadeproducto'),
    path('modulo-de-equipo/', equipo, name='equipo'),
    path('modulo-de-producto/', producto, name='producto'),
]