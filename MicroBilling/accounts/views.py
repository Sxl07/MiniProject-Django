# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts/login.html')  # Reemplaza 'home' con la URL a la que quieres redirigir después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('lista_insumos')  # Reemplaza 'home' con la URL a la que quieres redirigir después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    auth_logout(request)

def logout_view(request):
    logout(request)
    # redirige a la página de inicio, por ejemplo
    return redirect('login') 

@login_required
def my_protected_view(request):
    return render(request, 'accounts/protected_page.html')
