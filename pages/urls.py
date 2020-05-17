from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/procurar-medicamento', views.ajax_search_drug, name='procurar-medicamento'),
]