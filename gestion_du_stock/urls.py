from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('commande/', views.commande, name='commande'),
    path('devis/', views.devis, name='devis'),
    path('create_fournisseur/', views.create_fournisseur, name='create_fournisseur'),
    path('create_devis/',views.create_devis,name='create_devis'),
    path('add_details_devis/<int:devis_id>/', views.add_details_devis, name='add_details_devis'),
    path('error/', views.error, name='error'),
    path('create_produit/', views.create_produit, name='create_produit'),
    path('success/', views.error, name='success'),
    path('create_commande/', views.create_commande, name='create_commande'),
    path('add_details_commande/<int:commande_id>/', views.add_details_commande, name='add_details_commande'),
    path('create_facture/', views.create_facture, name='create_facture'),
    path('add_livraison/<int:facture_id>/', views.add_livraison, name='add_livraison'),
]
