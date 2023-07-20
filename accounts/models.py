from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    phone_mail = models.CharField(max_length=50, null=True, blank=True)
    cni = models.IntegerField( null=True, blank=True)
    Type_compte = models.CharField(max_length=20, null= True, blank=True)
    adresse = models.CharField(max_length= 100, null= True, blank=True)
    profession = models.CharField(max_length=50, null= True, blank=True)
    Zone = models.CharField(max_length=50, null=True, blank=True )
    Frais_tontine = models.IntegerField(null=True, blank=True)
    nom_garant = models.CharField(max_length=100, null=True, blank=True)
    prenom_garant = models.CharField(max_length=100, null=True, blank=True)
    cni_garant = models.IntegerField(null=True, blank=True)
    telephone_garant = models.IntegerField( null=True, blank=True)
    adresse_garant = models.CharField(max_length= 100, null= True, blank=True)
    profession_garant = models.CharField(max_length=20, null= True, blank=True)
    ceated_at = models.DateTimeField(auto_now_add=True)
    en_attente = models.CharField(max_length=20, default="en_attente", null=True, blank=True)



    def __str__(self):
        return f"{self.nom}"


class Client(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    identifiant = models.CharField(primary_key=True,max_length=10)
    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    phone_mail = models.CharField(max_length=50, null=True, blank=True)
    cni = models.IntegerField( null=True, blank=True)
    Type_compte = models.CharField(max_length=20, null= True, blank=True)
    adresse = models.CharField(max_length= 100, null= True, blank=True)
    profession = models.CharField(max_length=50, null= True, blank=True)
    Zone = models.CharField(max_length=50, null=True, blank=True )
    Frais_tontine = models.IntegerField(null=True, blank=True)
    nom_garant = models.CharField(max_length=100, null=True, blank=True)
    prenom_garant = models.CharField(max_length=100, null=True, blank=True)
    cni_garant = models.IntegerField(null=True, blank=True)
    telephone_garant = models.IntegerField( null=True, blank=True)
    adresse_garant = models.CharField(max_length= 100, null= True, blank=True)
    profession_garant = models.CharField(max_length=20, null= True, blank=True)
    ceated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom}"

class Agent(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    identifiant = models.CharField(primary_key=True,max_length=10)
    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length= 100, null= True, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    Telephone = models.CharField(max_length=50, null=True, blank=True)
    Zone = models.CharField(max_length=50, null=True, blank=True )
    cni = models.IntegerField( null=True, blank=True)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return f"{self.nom}"
    
    def get_clients(self):
        return self.clients.all()


class Payement(models.Model):
    client = models.ForeignKey('client', on_delete=models.CASCADE , null=True, blank=True)
    agent = models.ForeignKey('agent', on_delete=models.CASCADE , null=True, blank= True)
    montant_payement = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    date_payement = models.DateField(auto_now=True, null=True)
    nbr_jours = models.IntegerField(null=True, blank=True)
    jours_restant = models.IntegerField(null=True, blank=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    debut = models.BooleanField(null=True, blank=True)
    fin = models.BooleanField(null=True, blank=True)
    date_payement = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.client}"
    

class Compte(models.Model):
    client = models.ForeignKey('client', on_delete=models.CASCADE , null=True, blank=True)
    nom_type_compte = models.CharField(max_length=50, null=True, blank=True)
    solde_payement = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    date_payement = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.client}"


    


    
