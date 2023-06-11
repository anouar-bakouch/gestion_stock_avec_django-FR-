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

def success(request):
    return render(request, 'success.html')

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
            context = {'message': 'Ajouté'}
            return render(request, 'success.html', context)
    else:
        form = DetailsDevisForm(initial={'nDevis': devis.id})

    return render(request, 'devis/add_details_devis.html', {'form': form, 'devis': devis})

# create a produit 

def create_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'message': 'Produit ajouté'}
            return render(request, 'success.html', context)
    else:
        form = ProduitForm()
    return render(request, 'produit/create_produit.html', {'form': form})

# create a command 

def create_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'message': 'Commande ajoutée'}
            return render(request, 'success.html', context)
    else:
        form = CommandeForm()
    return render(request, 'commande/create_commande.html', {'form': form})

# add_details_commande

def add_details_commande(request, commande_id):
    try:
        commande = Commande.objects.get(pk=commande_id)
    except Commande.DoesNotExist:
        return redirect('create_commande')

    products = Produit.objects.all()
    if not products:
        # add a message to the context that no products exist
        context = {'message': 'No products exist'}
        return render(request, 'error.html', context)

    if request.method == 'POST':
        form = DetailCommandeForm(request.POST)
        if form.is_valid():
            details_commande = form.save(commit=False)
            details_commande.nCom = commande
            details_commande.save()
            context = {'message': 'Ajouté'}
            return render(request, 'success.html', context)
    else:
        form = DetailCommandeForm(initial={'nCom': commande.id})

    return render(request, 'commande/add_details_commande.html', {'form': form, 'commande': commande})


