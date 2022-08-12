
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
# Create your views here.
from .models import basic
from .forms import basicinfo


def index(request):
    return render(request, "termsgen/landing page/index.html")

def products(request):
    return render(request, "termsgen/products and templates/product.html")

def dashboard(request):
    return render(request, "termsgen/dashboard/dashboard.html")

def basic_info(request):
    submitted = False
    if request.method == "POST":
        form = basicinfo(request.POST)
        if form.is_valid():
            form.save
            return HttpResponseRedirect('/basic-info?submitted = True')
    else:
        form = basicinfo
        if 'submitted' in request.GET:
            submitted == True
    return render(request, "termsgen/dashboard/basic_info.html",{'form':form,'submitted':submitted})
    
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