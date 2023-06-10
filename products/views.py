from django.shortcuts import render
from django.http import HttpResponse
from .forms import FournisseurForm, DevisForm, ProduitForm, DetailsDevisForm, FactureForm, LivraisonForm, CommandeForm, DetailCommandeForm

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

def create_devis(request):
    if request.method == 'POST':
        form = DevisForm(request.POST)
        if form.is_valid():
            devis = form.save()
            return redirect('add_details_devis', devis_id=devis.id)  # redirect to a new URL with the 'devis_id' parameter
    else:
        form = DevisForm()
    return render(request, 'devis/create_devis.html', {'form': form})


def add_details_devis(request, devis_id):
    if request.method == 'POST':
        form = DetailsDevisForm(request.POST)
        if form.is_valid():
            details_devis = form.save(commit=False)
            details_devis.nDevis_id = devis_id  # set the nDevis foreign key to the devis_id parameter
            details_devis.save()
            return redirect('add_details_devis', devis_id=devis_id)  # redirect to the same URL to show the updated form
    else:
        form = DetailsDevisForm()
    return render(request, 'devis/add_details_devis.html', {'form': form})
