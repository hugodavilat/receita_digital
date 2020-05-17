from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import User

def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.user_type == 1:
                return redirect('procurar-paciente')
            else:
                return redirect('index')
        else:
            messages.error(request, 'Usuário e/ou senha incorreto(s).')
            return redirect('login')
    return render(request, 'accounts/login.html')

