from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *
from  .forms import CreateUserForm

def index(request):
    return render(request, "termsgen/landing page/index.html")

def getstarted(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "termsgen/sign in and signup pages/Get-Started.html", context)

def signin(request):
    context = {}
    return render(request, "termsgen/sign in and signup pages/Sign-In.html", context)
    
def products(request):
    return render(request, "termsgen/products and templates/product.html",)

def dashboard(request):
    products = Product.objects.all()

    return render(request, "termsgen/dashboard/edashboard.html", {'products':products})

def basic_info(request):
    return render(request, "termsgen/dashboard/basic_info.html")

def web_info(request):
    return render(request, "termsgen/dashboard/web_info.html")

def contact_us(request):
    return render(request, "termsgen/contact us page/contact_us.html")

def about_us(request):
    return render(request, "termsgen/about us page/about_us.html")

def privacy(request):
    return render(request, "termsgen/privacy policy page/index.html")

def previewdoc(request):
    return render(request, "termsgen/privacy policy page/previewdoc.html")

def downloadsuccess(request):
    return render(request, "termsgen/privacy policy page/downloadsuccess.html")

def additionalinfo(request):
    return render(request, "termsgen/privacy policy page/additionalinfo.html")

def security(request):
    return render(request, "termsgen/privacy policy page/security.html")

def return_and_refund(request):
    return render(request, 'termsgen/return and refund pages/Refund and Shipping Information.html')

def terms_and_conditions(request):
    return render(request, "termsgen/terms and condition/p1-business-info.html")