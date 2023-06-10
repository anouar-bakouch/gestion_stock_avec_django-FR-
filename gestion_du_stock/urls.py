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
]
