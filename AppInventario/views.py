from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate

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

def salir(request):
    #logout(request)
    print("LOGOUT CORRECTO")
    #return redirect("")