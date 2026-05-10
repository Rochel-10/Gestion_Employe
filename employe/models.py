from django.db import models

# Create your models here.
#c'est ici qu'on va definir la structure de notre model
#la class Employee va heriter de la class Model (models.Model)
#NB: on n'a pas creer un id car il est creer automatiquement par le model
#sin on veux personnaliser un id on peut utiliser le UU id qui est une série de char
#c a d des caracteres pour identifier de maniere unique un element dans la base de donnée
class Employe(models.Model):
    #Char: caracter, Field:champ, max_length: taille maximale
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    poste = models.CharField(max_length=100)
    #max_digits=10: nb total des chiffres, decimal_places=2: 2chiffres apres le virgule
    salaire = models.DecimalField(max_digits=10, decimal_places=2)

    #self: element courant
    def __str__(self):
        return self.nom


