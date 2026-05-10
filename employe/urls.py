#gerer les urls de notre application
#les urls va relier une page a une vue

from django.contrib import admin
#importer le path et l'include
from django.urls import path, include
#importer toutes les vues
from . import views

urlpatterns = [
    #le lien pour afficher la liste des utilisateurs a l'aide de l'objet liste_employes
    #on peut mettre un name du lien,
    path("", views.liste_employes, name="liste_employes"),
    #definir l'url pour acceder a la page du formrulaire
    #nouvelle fonction ajouter_employe, avec nom de la page ajouter_employe
    path("ajouter/", views.ajouter_employe, name="ajouter_employe"),
    #urls de modifier: fontion modifier_employe, et nom, page : modifier_employer
    #la modification se fera par id alors, /1, /2, /3,...
    path("modifier/<int:id>", views.modifier_employe, name="modifier_employe"),
    #url de supprimer avec l'id
    path("supprimer/<int:id>", views.supprimer_employe, name="supprimer_employe"),
]