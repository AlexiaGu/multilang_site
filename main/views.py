
from django.shortcuts import render, get_object_or_404

from main.models import Blog_Articles
from django.utils.translation import gettext_lazy as _
# from datetime import datetime



# Create your views here.

def index(request):
    
    #création d'une variable articles qui depuis le model récupère tout ce qu'il y a dans la table Blog_Articles
    context = {"articles": Blog_Articles.objects.all()}
    for article in context["articles"]:
        article.id = int(article.id)
        # date_string = article.publication_date.strftime("%d %m %Y")
        # day, month, year = map(int, date_string.split(" "))
        # article.publication_date = datetime(year, month, day)
    return render(request, "main/index.html", context)


def show(request, article_id):
    # get_object_or_404 permet ici d'afficher une erreur si l'id de l'objet voulu n'existe pas.
    # pk = primary key    
    context = {"article": get_object_or_404(Blog_Articles, pk = article_id)}
    return render(request, "main/show.html", context)