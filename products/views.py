from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'index.html')

def header(request):
    return render(request, 'header.html')

def footer(request):
    return render(request, 'footer.html')


