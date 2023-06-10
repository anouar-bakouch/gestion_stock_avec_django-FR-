from django import forms
from .models import Fournisseur, Devis, Produit, DetailDevis, Facture, Livraison, Commande, DetailCommande

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'

class DevisForm(forms.ModelForm):
    class Meta:
        model = Devis
        fields = '__all__'

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'

class DetailDevisForm(forms.ModelForm):
    class Meta:
        model = DetailDevis
        fields = '__all__'

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = '__all__'

class LivraisonForm(forms.ModelForm):
    class Meta:
        model = Livraison
        fields = '__all__'

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'

class DetailCommandeForm(forms.ModelForm):
    class Meta:
        model = DetailCommande
        fields = '__all__'

