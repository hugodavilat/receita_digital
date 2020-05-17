from django.shortcuts import render
from django.contrib import messages
from django.db import transaction

import string
import random
import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box

from doctors.models import Medico
from main.models import Medicamento, Posologia
from prescriptions.models import Receita
from patients.models import Paciente
from prescriptions.checker import check_key


def create_prescription(request):
    if request.method == "POST":
        patient_id = request.POST.get('id_paciente', None)
        drugs = request.POST.getlist('medicamentos')
        dosages = request.POST.getlist('posologias')
        observations = request.POST.get('observacoes', None)
        challenge_answer = request.POST.get('challenge-answer', None)
        current_user = request.user

        try:
            medico = Medico.objects.get(user_id=current_user.id)
            public_doctor = medico.chave_publica
            public_doctor = PublicKey(bytes.fromhex(public_doctor))
            challenge = request.session["challenge"]
            challenge_answer = bytes.fromhex(challenge_answer)
            check_result = check_key(public_doctor, challenge, challenge_answer)
            request.session["challenge"] = ""
            if not check_result:
                messages.error(request, "Falha na autenticação")
                context = {
                    'id_paciente': patient_id,
                    'medicamentos': [(drug, dosages[i]) for i, drug in enumerate(drugs)],
                    'observacoes': observations
                 }
                return render(request, 'prescriptions/create_prescription.html', context)

            patient = Paciente.objects.get(pk=patient_id) 
             # Pegar objeto do médico
            with transaction.atomic():
                receita = Receita(
                    paciente=patient,
                    observacoes=observations,
                    medico=medico
                )
                receita.save()
                for drug, dosage in zip(drugs, dosages):
                    medicamento, _ = Medicamento.objects.get_or_create(
                        nome=drug
                    )
                    posologia, _ = Posologia.objects.get_or_create(
                        medicamento=medicamento,
                        posologia=dosage,
                    )
                    receita.posologias.add(posologia)

        except Paciente.DoesNotExist as e:
            messages.error(request, 'Paciente não encontrado')
            context = {
                'id_paciente': patient_id,
                'medicamentos': [(drug, dosages[i]) for i, drug in enumerate(drugs)],
                'observacoes': observations
            }
            return render(request, 'prescriptions/create_prescription.html', context)
    challenge = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))
    request.session['challenge'] = challenge
    context = {
        'challenge': challenge
    }
    return render(request, 'prescriptions/create_prescription.html', context)


def get_prescription(request):
    context = {}
    if request.method == "POST":
        receita_id = request.POST.get('receita_id', None)
        if request.POST.get("vende", False):
            if Receita.objects.filter(id=receita_id).exists():
                receita = Receita.objects.get(pk=receita_id)
                receita.used = True
                receita.save()
                context['receita'] = receita
                messages.success(request, 'Receita utilizada com sucesso.')
            else:
                context['receita_id'] = receita_id
                messages.error(request, 'Receita não encontrada.')
        elif request.POST.get("busca", False):
            if Receita.objects.filter(id=receita_id).exists():
                receita = Receita.objects.get(pk=receita_id)
                if receita.used == True:
                    messages.warning(request, 'Receita já utilizada.')
                context['receita'] = receita
            else:
                context['receita_id'] = receita_id
                messages.error(request, 'Receita não encontrada')
    return render(request, 'prescriptions/farmacia.html', context)