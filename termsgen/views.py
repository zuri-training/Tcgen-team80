from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "termsgen/landing page/index.html")

def products(request):
    return render(request, "termsgen/products and templates/product.html")

def dashboard(request):
    return render(request, "termsgen/dashboard/dashboard.html")

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

