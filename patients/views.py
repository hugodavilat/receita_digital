from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Paciente

def create_patient(request):
    if request.method == 'GET':
        return render(request, 'patients/create_patient.html')
    else:
        id_paciente     = request.POST.get('id-paciente')
        nome            = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        telefone        = request.POST.get('telefone')
        cpf             = request.POST.get('cpf')
        email           = request.POST.get('email')

        # Conferir se cartao sus existe
        if Paciente.objects.filter(id_paciente=id_paciente).exists():
            messages.add_message(request, 40, 'Cartão SUS já cadastrado.')
            return render(request, 'patients/create_patient.html')
        else:
            new_paciente = Paciente(
                id_paciente=id_paciente,
                nome=nome,
                data_nascimento=data_nascimento,
                telefone=telefone,
                cpf=cpf,
                email=email
            )
            try:
                new_paciente.save()
                return redirect('/medico/procurar-paciente')
            except Exception as e:
                messages.add_message(request, 40, e)
                return render(request, 'patients/create_patient.html')
