from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from AppInventario.views import login_web, index, tipo_de_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_web, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('index/', index),
    path('tipo-de-producto/', tipo_de_producto, name='tipo_de_producto'),
]