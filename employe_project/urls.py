"""
URL configuration for employe_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#importer le path et l'include
from django.urls import path, include

urlpatterns = [
    #un chemin creer pardefaut par django
    #admin/: la page administrateur de notre site
    path('admin/', admin.site.urls),
    #inclure les urls dans l'application employe dans le projet projet_employe
    # avec "" le rien apres le localhost.../8000
    #inclure le chemin depuis employe/urls.py
    path("", include('employe.urls'))


]
