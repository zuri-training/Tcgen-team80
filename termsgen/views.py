from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, this page works")


def products(request):
    return render(request, "termsgen/products and templates/product.html")
