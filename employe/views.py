#from Scripts.bottle import redirect
from django.shortcuts import render , redirect, get_object_or_404
#importer le model 'Employe' pour etre connue dans notre views
#au lieu de mettre *(tous) on va mettre Employe car importer lui seule
from .models import Employe
#on va importer le formulaire qu'on a creer
from .forms import EmployeForm

# Create your views here.
#creer l'interface qu'on va voir en premier
#qui va contenir la liste des employe

#le view va representer la logique de notre application
#on va creer une fonction qui va recuperer la liste de tous les employes

#fonction pour la liste des employes
#qui va prendre en argument un requete
#la fonction et les instructions qui va recuperer la liste des employe
#depuis la base de donnée et l'afficher dans une interface HTML
def liste_employes(request):
    #on va recuperer tous les employes dans notre site avec le syntaxe avec .objects.all
    #creer une variable employes pour sotcker le model Employe
    employes = Employe.objects.all()
    #envoyer la liste des emplyes a une page HTML
    #utiliser la fonction render pour rendre a une page
    #argumemt: request , la page(chemin), passer le données a afficher dans cette page
    #donnees ici la liste des employes en json : variable employes
    return render(request, 'employe/list.html', {'employes': employes})

#fonction qui va faire l'ajouter des employes
def ajouter_employe(request):
    #on va recuperer le formulaire
    #l'utilisateur va soumettre pour afficher la liste des utilisateurs a l'aide de la formulaire
    #la formulaire qu'on va recuperer sera de form EmployeForm
    #*le methode GET qui permet de recuperer des informations
    #*la methode POST qui permet d'envoyer des informations
    #pour envoyer des information a notre vieuw, on va utiliser la methode POST(request.POST or None)
    #ou None si on se sais pas
    form = EmployeForm(request.POST or None)
    #on va verifier si notre info est valide(si la taille max des entrer ne depasse pas)
    if form.is_valid():
        #si valide, alors enregistrer les info dans la base de données
        form.save()
        #apres enregistrement, redirection sur la page des listes des employes
        return redirect('liste_employes')
    #si non, returner a la page du formulaire qu'on va encore creer
    return render(request, 'employe/formulaire.html', {'form': form})

#la class modifier
def modifier_employe(request, id):
    #recuperer l'employe a modifier afin de remplir, afin de remplir par defaut le formulaire
    #avec ces informations
    #get_object_or_404: c'est un fonction qui permet de recuperer un objet c'est a d des données
    # de la base de donnée et va returner 404 not found si' il ne le voit pas
    #preciser dans la l'argument les données a recuperer, ici(l'employe et son id)
    employe = get_object_or_404(Employe, id=id)
    #on va generer un autre formulaire,
    #et remplir ce formulaire la par defaut par les informations de l'employé(instance=employe)
    form = EmployeForm(request.POST or None, instance=employe)
    # on va verifier si notre info est valide(si la taille max des entrer ne depasse pas)
    if form.is_valid():
        # si valide, alors enregistrer les info dans la base de données
        form.save()
        # apres enregistrement, redirection sur la page des listes des employes
        return redirect('liste_employes')
    # si non, retourner a la  meme page de formulaire
    return render(request, 'employe/formulaire.html', {'form': form})

def supprimer_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    #verification
    #request.method: un formulaire qui va confirmer la suppression ou non
    #verification si la requete qu'on a envoyé vient d'une methode POST, dans confirmer_suppression
    #si oui alors il va le supprimer
    if request.method == 'POST':
        employe.delete()
        return redirect('liste_employes')
        #on va etre rediriger dans une nouvelle page, qui va afficher les informations
        #dans une page de confirmation
    return render(request, 'employe/confirmer_suppression.html', {'employe': employe})











