from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def medico(request):
    return render(request, 'pages/index.html')

def criar_paciente(request):
    return render(request, 'pages/index.html')

def receita(request):
    return render(request, 'pages/index.html')

def farmacia(request):
    return render(request, 'pages/index.html')