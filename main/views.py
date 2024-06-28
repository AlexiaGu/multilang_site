from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    # Récupération de ce message dans le fichier views.py de main
    context = {"message": "Bello !"}
    # pour récuperer le template main
    template = loader.get_template("main/index.html")
    return HttpResponse(template.render(context, request))