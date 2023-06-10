from django.contrib import admin

# Register your models here.

from .models import Fournisseur, Devis, Produit, DetailDevis, Facture, Livraison, Commande, DetailCommande

admin.site.register(Fournisseur)
admin.site.register(Devis)
admin.site.register(Produit)
admin.site.register(DetailDevis)
admin.site.register(Facture)
admin.site.register(Livraison)
admin.site.register(Commande)
admin.site.register(DetailCommande)

