from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from AppInventario.views import login_web, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_web, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('index/', index),
]