from django.shortcuts import render

def search_patient(request):
    return render(request, 'doctors/search_patient.html')