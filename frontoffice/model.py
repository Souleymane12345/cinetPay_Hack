from django.db import models

# Create your models here.
class CommonData (models.Model):
    email = models.EmailField(max_length=225)
    numero = models.ImageField()
    password = models.CharField(max_length= 50)
    address = models.CharField(max_length=100)
   


    class Meta: 
        abstract:True

class Users(CommonData):
    
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=50)
    compte = models.CharField(max_length=25)
    montant = models.IntegerField()
    identifiant = models.CharField(max_length=25)

    
    



