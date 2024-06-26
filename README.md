# multilang_site

L’exercice était de réussir à créer un projet nommé multilang_site contenant une application Main avec le framework Django de Python. Cette application doit pouvoir permettre la traduction d’information statique et dynamique selon la langue que l’on souhaite. Des applications Large Language Models (LLM) étaient éventuellement attendues.

Statut du projet :
Le projet est encore en cours de développement et nécessite encore des ajouts et corrections.

Par exemple:
Au niveau de la date de publications de l’article, je n’arrivais pas à récuperer la date le navigateur m’indiquant Je me suis aidé de ChatGPT pour essayer de régler cela et malheureusement sans succès. J’ai effectué plusieurs tests qui ne m’ont pas permis de récupérer les dates indiquées dans ma base de données. Afin de pouvoir continuer à avancer sur mon projet, j’ai commenté le champ publication_date dans le fichier models.py

Au niveau de la traduction du site, j’ai également quelques difficultés. Par exemple, lorsque je suis sur la page d’accueil, j'arrive à modifier au clic sur des boutons la langue que je souhaitais employée pour l’affichage. Ainsi mon titre ainsi que les boutons s’adapté selon la langue voulu. Il se trouve qu’au fur et à mesure du développement une erreur me permet de modifier la langue indiqué dans la barre d’url mais les boutons ne se mettent plus à jour et le titre static reste en anglais en changeant seulement un mot. J’ai effectué des essais dans le fichier django.po du dossier “locale” au niveau des traductions et en lançant la commande django-admin compilemessages sans changement

Du côté du template show.html pour afficher les articles. J’ai par exemple fait l’utilisation de la balise {% trans “Contenu” %} mais cela m'affiche une erreur dans le navigateur.
J’ai trouvé grâce à chatGPT, l’ajout de l’élément de traduction suivant
La traduction fonctionne sur le mot “contenu”, cependant je n’arrive plus à récupérer le contenu de mon article dans la base de données. J’ai effectué des modifications et recherches entre autres avec ChatGPT mais sans succès.

Ci-dessous les dépendances utilisées lors du développement:
asgiref==3.3.1
certifi==2020.12.5
chardet==4.0.0
Django==3.1.6
django-i18next==0.1.3
django-nine==0.2.7
django-rosetta==0.9.5
gunicorn==22.0.0
idna==2.10
Jinja2==3.1.4
MarkupSafe==2.1.5
packaging==24.1
polib==1.1.0
python-environ==0.4.54
pytz==2021.1
requests==2.25.1
setuptools==70.1.1
six==1.15.0
soupsieve==2.5
sqlparse==0.4.1
tzdata==2024.1
urllib3==1.26.3
waitress==3.0.0

Certaines ne seront au final pas exploitées ayant fait des essais pour régler certains de mes problèmes ou n’étant je pense pas assez bien exploitée par moi.
Par exemple :
gunicorn => pour le déploiement avec render. Cela n’a pas pu aboutir ayant fait plusieurs tests et modifications et cela ne fonctionne pas sous Windows.
Jinja2 => Jinja2 avait été ajouté dans le but de régler un problème d’affichage de date, le modèle gérant les articles de blog contenant une date de publication.

Instructions d’installation et d’utilisation :

Afin de pouvoir récupérer et lancer ce projet, il sera nécessaire de cloner le repository sur Github et ensuite de suivre les commandes suivantes dans le terminal :
Lien github : https://github.com/AlexiaGu/multilang_site
Copier le lien du code SSH
Et effectuer la commande suivante dans le terminal :
git clone git@github.com:AlexiaGu/multilang_site.git

Ensuite il sera nécessaire de se placer dans le dossier en utilisant la commande :
cd multilang_site

Il sera nécessaire d’installer les dépendances du projet :
pip install -r requirements.txt

D’effectuer la migrations de la base de données :
python manage.py migrate

Et de lancer le serveur de développement pour l’affichage dans le navigateur:
python manage.py runserver

Technologies utilisées :
Dans le cadre de ce projet, j’ai pu utiliser le framework Django et son système d’internationalisation “i18n” en me basant sur la documentation de Django :
Traduction | Documentation de Django | Django (djangoproject.com)
Ainsi qu’en suivant des vidéos youtube :
https://www.youtube.com/watch?v=RWvn-IgRUv0
https://www.youtube.com/watch?v=AlJ8cGbk8ps&t=302s

Pour ma tentative de déploiement avec Render, j’ai trouvé cette documentation provenant du site Medium :
https://medium.com/@MsrVolt/d%C3%A9ployer-une-application-django-sur-render-gratuitement-en-quelques-minutes-27ade87b95ce

J’ai également essayé le déploiement avec pythonwhere, en suivant le tutoriel suivant :
https://www.docstring.fr/blog/deployer-une-application-django-sur-pythonanywhere/

Pour la base de donnée, j'ai utilisé Beekeeper Studio :
https://www.beekeeperstudio.io/

Lors de l’élaboration de ce test, j’ai rencontré beaucoup de défis. Python est un langage que je n’avais jamais abordé et je ne connaissais donc pas le framework Django associé.
Afin de savoir par où débuter ce projet, j’ai demandé à TchatGPT comment procéder et il en est ressorti que je devais voir les bases de Python. J’ai donc pris le temps de me renseigner en l’occurrence en faisant des exercice sur les bases de Python avec Codeacademy :
https://www.codecademy.com/catalog/language/python

Ensuite pour Django, je me suis aidée de la documentation ainsi que des vidéos youtube :
https://docs.djangoproject.com/en/5.0/
https://www.youtube.com/watch?v=iBGhDHtysAA&list=PLrSOXFDHBtfED_VFTa6labxAOPh29RYiO

J’ai pu passer beaucoup de temps pour essayer de régler certains problèmes que j’ai réussi à solutionner comme par exemple, lorsque l’on est sur la page des articles et que l’on souhaite traduire un élément static, pouvoir rester sur la page sans être redirigé sur la page d’accueil.

Pour d’autres, comme pour la mise en place de la traduction, j’ai pu perdre beaucoup de temps en recommençant plusieurs fois cette mise en place. Sur certaines facettes, cela m’a montré que pousser son travail de façon régulière lorsque quelque chose fonctionne est important.

Parmis mes axes d’amélioration sur mon travail, il y aurait par exemple:

- Créer des branches différentes en les nommant selon la partie sur laquelle je travaille,
- Créer une branche “dev”, afin de pousser son travail dessus et pas directement sur la branche principale “main”,
- Ne pas oublier le fichier .gitignore avant de pousser mon travail,
- Utiliser de façon plus productive ChatGPT car je ne l’interroge pas de façon optimale,
- Rédiger le fichier README au fur et à mesure de mon travail et des ajout sur Github,
- Améliorer l’aspect visuel et le responsive du site,
- Reprendre le déploiement,
- Reprendre la documentation Django code sur la partie traduction pour reprendre mon code.

Je n'ai pas eu l’occasion de regarder l’intégration et l’utilisation efficace des modèles de langage pour le chatbot et/ou RAG n’ayant pas atteint les objectifs pour la partie traduction.

Au vu des améliorations à apporter à mon projet, je suis ouverte à tous conseils pouvant me permettre de le porter à bien et de m’améliorer. Je souhaite comprendre ce que je peux apporter à ce projet et le déploiement.
