from django.urls import path

from . import views

urlpatterns = [
    path('procurar-paciente', views.search_patient, name='procurar-paciente'),
    path('adicionar-medico', views.create_doctor, name='adicionar-medico')
]