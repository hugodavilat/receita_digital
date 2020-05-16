from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login', views.login),
    path('medico', views.medico),
    path('farmacia', views.farmacia)
]