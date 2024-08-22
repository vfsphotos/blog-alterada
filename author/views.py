from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import AuthenticationForm, AuthorCreationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('publication-list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('publication-list')

def register_view(request):
    if request.method == 'POST':
        form = AuthorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = AuthorCreationForm()
    return render(request, 'register.html', {'form': form})