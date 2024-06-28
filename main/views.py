from django.shortcuts import render
from django.http import HttpResponse

from main.models import Blog_Articles



# Create your views here.

def index(request):
    #création d'une variable articles qui depuis le model récupère tout ce qu'il y a dans la table Blog_Articles
    context = {"articles": Blog_Articles.objects.all()}
    return render(request, "main/index.html", context)