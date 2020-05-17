from django.shortcuts import render
from django.http import JsonResponse
from main.models import Medicamento

def index(request):
    return render(request, 'pages/index.html')

def ajax_search_drug(request):
    name = request.GET.get('nome', None)
    matches = list(Medicamento.objects.filter(nome__icontains=name).values_list('nome', flat=True))
    data = {
        'nomes': matches
    }
    return JsonResponse(data)
