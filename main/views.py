
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from main.models import Blog_Articles



# Create your views here.

def index(request):
    #création d'une variable articles qui depuis le model récupère tout ce qu'il y a dans la table Blog_Articles
    context = {"articles": Blog_Articles.objects.all()}
    return render(request, "main/index.html", context)

def show(request, article_id):
    # get_object_or_404 permet ici d'afficher une erreur si l'id de l'objet voulu n'existe pas.
    # pk = primary key    
    context = {"article": get_object_or_404(Blog_Articles, pk = article_id)}
    return render(request, "main/show.html", context)