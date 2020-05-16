from django.urls import path

from . import views

urlpatterns = [
    path('adicionar-paciente', views.create_patient, name='adicionar-paciente'),
]