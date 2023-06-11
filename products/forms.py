from django import forms
from .models import Fournisseur, Devis, Produit, DetailDevis, Facture, Livraison, Commande, DetailCommande
# create a Fournisseur Form with bootstrap

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

class DetailsDevisForm(forms.ModelForm):
    class Meta:
        model = DetailDevis
        fields = ['nDevis', 'RefProd', 'qteProd', 'prixProd']
        widgets = {
            'nDevis': forms.Select(attrs={'class': 'form-control'}),
            'RefProd': forms.Select(attrs={'class': 'form-control'}),
            'qteProd': forms.NumberInput(attrs={'class': 'form-control'}),
            'prixProd': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nDevis'].queryset = Devis.objects.all()
        self.fields['nDevis'].empty_label = None
        self.fields['RefProd'].queryset = Produit.objects.all()
        self.fields['RefProd'].empty_label = None
        self.fields['RefProd'].label_from_instance = lambda obj: obj.description


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
        widgets = {
            'RefProd': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'marque': forms.TextInput(attrs={'class': 'form-control'}),
        }
    

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
        widgets = {
            'nCom': forms.TextInput(attrs={'class': 'form-control'}),
            'dateCom': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'YYYY-MM-DD'}),
            'nFr': forms.Select(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
            'refDevis': forms.Select(attrs={'class': 'form-control'}),
        }

class DetailCommandeForm(forms.ModelForm):
    class Meta:
        model = DetailCommande
        fields = '__all__'
        widgets = {
            'nCom': forms.Select(attrs={'class': 'form-control'}),
            'nProd': forms.Select(attrs={'class': 'form-control'}),
            'qteCde': forms.NumberInput(attrs={'class': 'form-control'}),
            'prixProd': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        

