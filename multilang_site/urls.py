
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    # route pour accéder à l'application
    path('', include('main.urls') )
)

