from django.db import models

# Create your models here.

class Fournisseur(models.Model):
    nFr = models.IntField(max_length=50)
    Societe = models.CharField(max_length=50)
    tel = modes.IntField(max_length=14)
    email = models.EmailField(max_length=50)
    adresse = models.CharField(max_length=50)

class Devis(models.Model) :
    nDevis = models.IntField(max_length = 50)
    dateDevis = models.DateField()
    montant = models.FloatField(max_length = 50)
    nFr = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

class Produit(models.Model) :
    RefProd = models.CharField(max_length = 50)
    description = models.CharField(max_length = 50)
    marque = models.CharField(max_length = 50)

class DetailDevis(models.Model) :
    qteProd = models.IntField(max_length = 50)
    prixProd = models.FloatField(max_length = 50)
    nDevis = models.ForeignKey(Devis, on_delete=models.CASCADE)
    RefProd = models.ForeignKey(Produit, on_delete=models.CASCADE)

class Facture(models.Model) :
    nFact = models.IntField(max_length = 50)
    dateFact = models.DateField()
    montantFact = models.FloatField(max_length = 50)
    nFr = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

class Livraison(models.Model) :
   nBon = models.IntField(max_length = 50)
   qteLiv = models.IntField(max_length = 50)
   prixLiv = models.FloatField(max_length = 50)
   RefFact = models.ForeignKey(Facture, on_delete=models.CASCADE)
   RefProd = models.ForeignKey(Produit, on_delete=models.CASCADE)

class Commande(models.Model) :
    nCom = models.IntField(max_length = 50)
    dateCom = models.DateField()
    montantCde = models.FloatField(max_length = 50)
    nFr = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    refDevis = models.ForeignKey(Devis, on_delete=models.CASCADE)

class DetailCommande(models.Model) :
    qteCde = models.IntField(max_length = 50)
    prixProd = models.FloatField(max_length = 50)
    nCom = models.ForeignKey(Commande, on_delete=models.CASCADE)
    RefProd = models.ForeignKey(Produit, on_delete=models.CASCADE)

