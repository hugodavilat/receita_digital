from django.shortcuts import render, redirect
from django.contrib import messages

from main.models import Paciente

def search_patient(request):
    if request.method == "POST":
        patient_id = request.POST['id-paciente']
        try:
            patient = Paciente.objects.get(pk=patient_id)
            return redirect('criar-receita')
        except Paciente.DoesNotExist as e:
            messages.error(request, 'Paciente não encontrado')
            return redirect('adicionar-paciente')

    return render(request, 'doctors/search_patient.html')
