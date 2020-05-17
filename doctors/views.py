from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.models import User
from doctors.models import Medico
from patients.models import Paciente

def search_patient(request):
    if request.method == "POST":
        patient_id = request.POST.get('id-paciente')
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
        id_medico       = request.POST.get('id-medico')
        username        = request.POST.get('username')
        if Medico.objects.filter(crm=id_medico).exists():
            messages.add_message(request, 40, 'CRM já cadastrado.')
            return render(request, 'doctors/create_doctor.html')
        if User.objects.filter(username=username).exists():
            messages.add_message(request, 40, 'Username já existente')
            return render(request, 'doctors/create_doctor.html')
        else:
            medico_data = {k:v[0] for k,v in dict(request.POST).items()}
            try:
                Medico.create(**medico_data)
                return redirect('/medico/procurar-paciente')
            except Exception as e:
                messages.add_message(request, 40, e)
                return render(request, 'patients/create_patient.html')