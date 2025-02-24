from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro realizado com sucesso! Faça login.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'login_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu')
        else:
            # Adiciona a mensagem de erro
            messages.error(request, 'Por favor, entre com um usuário e senha corretos.')
    else:
        form = LoginForm()
    return render(request, 'login_app/login.html', {'form': form})

def menu_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'login_app/menu.html')