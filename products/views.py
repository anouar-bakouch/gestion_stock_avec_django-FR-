from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .forms import FournisseurForm, DevisForm, ProduitForm, DetailsDevisForm, FactureForm, LivraisonForm, CommandeForm, DetailCommandeForm
from .models import Devis,Produit

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

def error(request):
    return render(request, 'error.html')

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
            return redirect('add_details_devis', devis_id=devis.id)
    else:
        form = DevisForm()
    return render(request, 'devis/create_devis.html', {'form': form})



def add_details_devis(request, devis_id):
    try:
        devis = Devis.objects.get(pk=devis_id)
    except Devis.DoesNotExist:
        return redirect('create_devis')

    products = Produit.objects.all()
    if not products:
        # add a message to the context that no products exist
        context = {'message': 'No products exist'}
        return render(request, 'error.html', context)

    if request.method == 'POST':
        form = DetailsDevisForm(request.POST)
        if form.is_valid():
            details_devis = form.save(commit=False)
            details_devis.nDevis = devis
            details_devis.save()
            return redirect('add_details_devis', devis_id=devis_id)
    else:
        form = DetailsDevisForm(initial={'nDevis': devis.id})

    return render(request, 'devis/add_details_devis.html', {'form': form, 'devis': devis})