from django.db import models


# Create your models here:

class Author(models.Model):
    name = models.CharField(max_length = 64, unique = True)

class Blog_Articles(models.Model):
    # champs contenu dans le model
    title = models.CharField(max_length= 100, unique = True)
    content = models.CharField(max_length=300, unique = True)
    # publication_date = models.DateField(auto_now_add=True)
   
    # clé étrangère venant d'un autre table
    author = models.ForeignKey(Author, on_delete= models.DO_NOTHING)
