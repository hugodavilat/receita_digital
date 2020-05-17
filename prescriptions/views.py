from django.shortcuts import render
from prescriptions.models import Receita
from patients.models import Paciente
from django.contrib import messages

def create_prescription(request):
    if request.method == "POST":
        patient_id = request.POST.get('id_paciente', None)
        drugs = request.POST.getlist('medicamentos')
        dosages = request.POST.getlist('posologias')
        observations = request.POST.get('observacoes', None)

        try:
            patient = Paciente.objects.get(pk=patient_id)
            # Pegar objeto do médico
            receita = Receita(
                paciente=patient,
                observacoes=observations,
                medico=None,
                documento=None,
                signature=None
            )
            # Criar remédios se não exitirem
            # Adicionar posologias
            # Salvar receitas
        except Paciente.DoesNotExist as e:
            messages.error(request, 'Paciente não encontrado')
            context = {
                'id_paciente': patient_id,
                'medicamentos': [(drug, dosages[i]) for i, drug in enumerate(drugs)],
                'observacoes': observations
            }
            return render(request, 'prescriptions/create_prescription.html', context)

    return render(request, 'prescriptions/create_prescription.html')