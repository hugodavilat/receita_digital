from django.urls import path

from . import views

urlpatterns = [
    path('criar-paciente', views.create_patient, name='criar-paciente'),
]