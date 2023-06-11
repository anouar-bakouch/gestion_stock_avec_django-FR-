from django.shortcuts import render,redirect,render_to_response
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
        return redirect('create_devis')  # redirect to create_devis view if the requested devis_id does not exist

    products = Product.objects.all()
    if not products:
        return render_to_response('error.html', {'message': 'No products exist.'})  # render an error message if no products exist

    if request.method == 'POST':
        form = DetailsDevisForm(request.POST)
        if form.is_valid():
            details_devis = form.save(commit=False)
            details_devis.nDevis = devis  # set the nDevis foreign key to the Devis object
            details_devis.save()
            return redirect('add_details_devis', devis_id=devis_id)
    else:
        form = DetailsDevisForm(initial={'nDevis': devis.id})  # set the initial value of nDevis to the id of the Devis instance
    return render(request, 'devis/add_details_devis.html', {'form': form, 'devis': devis})