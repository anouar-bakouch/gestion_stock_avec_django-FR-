from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('commande/', views.commande, name='commande'),
    path('devis/', views.devis, name='devis'),
    path('create_fournisseur/', views.create_fournisseur, name='create_fournisseur'),
]
