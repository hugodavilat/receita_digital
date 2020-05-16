from django.urls import path

from . import views

urlpatterns = [
    path('criar-receita', views.create_prescription, name='criar-receita'),
]