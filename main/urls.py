# Routage de l'application

from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # définition d'une vue pour l'affichage
    # utile pour faire des urls
path('', views.index, name='index'), # main/ page d'accueil
# <int:article_id>/ correspond à la route qui sera un nombre entier 
path('<int:article_id>/', views.show, name='show'), # main/<id
]
