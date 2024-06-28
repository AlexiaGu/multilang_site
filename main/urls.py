# Routage de l'application

from django.urls import path
from . import views

urlpatterns = [
    #  définition d'une vue pour l'affichage
path('', views.index, name='index')
]
