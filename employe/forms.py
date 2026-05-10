#on va creer un formulaire, jdango va le creer automatiquement
#le formulaire sert a: ajouter un nouvel employé, modification de ce meme employé
from django import forms
#importer le models pour faire voir a quoi ressemblerai le formulaire
from .models import Employe

#ici il est heriter d'un formulaire par defaut(forms.ModelForm)
#django creer automatiquement un formulaire basé sur le modèle
class EmployeForm(forms.ModelForm):
    class Meta:
        #le formulaire aura rapport au modele
        model = Employe
        #les champs que le formulaire doit comporter
        fields = ['nom', 'email', 'poste','salaire']
        #rajouter une nouvelle class qui s'appelle widget, qui permet d'ajouter des class  name
        #des classes directement aux elements de notre formulaire
        widgets = {
            'nom': forms.TextInput(attrs= {
                'class':'input w-full',
                'placeholder': 'Nom'
            }),
            'email': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Email'
            }),
            'poste': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Poste'
            }),
            'salaire': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Salaire'
            })
        }

