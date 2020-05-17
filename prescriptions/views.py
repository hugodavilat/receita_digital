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


def get_prescription(request):
    if request.method == "POST":
        receita_id = request.POST.get('receita_id')
        print(receita_id)

        if Receita.objects.filter(id=receita_id).exists():
            receita = Receita.objects.get(pk=receita_id)
            context = {
                'medico': receita.medico.nome
            }
            return render(request, 'prescriptions/farmacia.html', context)
        else:
            messages.error(request, 'Receita não Encontrada')
    return render(request, 'prescriptions/farmacia.html')