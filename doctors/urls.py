from django.urls import path

from . import views

urlpatterns = [
    path('procurar-paciente', views.search_patient, name='procurar-paciente'),
]