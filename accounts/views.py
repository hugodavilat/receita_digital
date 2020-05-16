from django.shortcuts import render, redirect

def login(request):
    return redirect('procurar-paciente')
