from django.shortcuts import render
from django.http import HttpResponse
from .forms import FournisseurForm, DevisForm, ProduitForm, DetailDevisForm, FactureForm, LivraisonForm, CommandeForm, DetailCommandeForm

# Create your views here.

def home(request):
    return render(request, 'main.html')

def header(request):
    return render(request, 'header.html')

def footer(request):
    return render(request, 'footer.html')

def commande(request):
    return render(request, 'commande/commande.html')

def devis(request):
    return render(request, 'devis/devis.html')

def fournisseur(request):
    return render(request, 'fournisseur/create_fournisseur.html')

# creating a fournisseur

def create_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Fournisseur enregistré')
    else:
        form = FournisseurForm()
    return render(request, 'fournisseur/create_fournisseur.html', {'form': form})

# creating a devis

def create_devis(request) :
    if request.method == 'POST' :
        form = DevisForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Devis enregistré')
    else :
        form = DevisForm()
    return render(request,'devis/create_devis.html',{'form':form})
