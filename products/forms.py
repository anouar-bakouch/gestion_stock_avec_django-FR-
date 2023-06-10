from django import forms
from .models import Fournisseur, Devis, Produit, DetailDevis, Facture, Livraison, Commande, DetailCommande

# create a Fournisseur Form with bootstrap
from django import forms
from .models import Fournisseur

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nFr', 'Societe', 'tel', 'email', 'adresse']
        widgets = {
            'nFr': forms.TextInput(attrs={'class': 'form-control'}),
            'Societe': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'})
        }

class FournisseurChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.nFr)

class DevisForm(forms.ModelForm):
    nFr = FournisseurChoiceField(queryset=Fournisseur.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}), to_field_name='nFr')
    
    class Meta:
        model = Devis
        fields = ['nFr','dateDevis','nDevis','montant']
        widgets = {
            'dateDevis': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'YYYY-MM-DD'}),
            'nFr': forms.Select(attrs={'class': 'form-control'}),
            'nDevis': forms.TextInput(attrs={'class': 'form-control'}),
            'montant': forms.TextInput(attrs={'class': 'form-control'}),
        }

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

