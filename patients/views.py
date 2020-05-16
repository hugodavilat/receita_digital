from django.shortcuts import render

def create_patient(request):
    return render(request, 'patients/create_patient.html')
