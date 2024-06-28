# Routage de l'application

from django.urls import path
from . import views

urlpatterns = [
    #  définition d'une vue pour l'affichage
    # utile pour faire des urls
path('', views.index, name='indexOfMain')
]
