from django.db import models

# Create your models here.

class Fournisseur(models.Model):
    nFr = models.IntegerField()
    Societe = models.CharField(max_length=50)
    tel = models.IntegerField()
    email = models.EmailField(max_length=50)
    adresse = models.CharField(max_length=50)

class Devis(models.Model) :
    nDevis = models.IntegerField()
    dateDevis = models.DateField()
    montant = models.FloatField(max_length = 50)
    nFr = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

class Produit(models.Model) :
    RefProd = models.CharField(max_length = 50)
    description = models.CharField(max_length = 50)
    marque = models.CharField(max_length = 50)

class DetailDevis(models.Model) :
    qteProd = models.IntegerField()
    prixProd = models.FloatField(max_length = 50)
    nDevis = models.ForeignKey(Devis, on_delete=models.CASCADE)
    RefProd = models.ForeignKey(Produit, on_delete=models.CASCADE)

class Facture(models.Model) :
    nFact = models.IntegerField()
    dateFact = models.DateField()
    montantFact = models.FloatField(max_length = 50)
    nFr = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

class Livraison(models.Model) :
   nBon = models.IntegerField()
   qteLiv = models.IntegerField()
   prixLiv = models.FloatField(max_length = 50)
   RefFact = models.ForeignKey(Facture, on_delete=models.CASCADE)
   RefProd = models.ForeignKey(Produit, on_delete=models.CASCADE)

class Commande(models.Model) :
    nCom = models.IntegerField()
    dateCom = models.DateField()
    montantCde = models.FloatField(max_length = 50)
    nFr = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    refDevis = models.ForeignKey(Devis, on_delete=models.CASCADE)

class DetailCommande(models.Model) :
    qteCde = models.IntegerField()
    prixProd = models.FloatField(max_length = 50)
    nCom = models.ForeignKey(Commande, on_delete=models.CASCADE)
    RefProd = models.ForeignKey(Produit, on_delete=models.CASCADE)

