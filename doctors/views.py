from django.shortcuts import render, redirect
from django.contrib import messages

from patients.models import Paciente
from doctors.models import Medico

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

def create_doctor(request):
    if request.method == 'GET':
        return render(request, 'doctors/create_doctor.html')

    if request.method == 'POST':
        pass