
from tokenize import group

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect

# Create your views here.

from .models import basic
from .forms import basicinfo


# Create your views here.

from .models import *
from .forms import CreateUserForm

from .decorators import unauthenticated_user, allowed_users, admin_only

def index(request):
    return render(request, "termsgen/landing page/index.html")

@unauthenticated_user
def getstarted(request):
    
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name= 'customer')
                user.groups.add(group)

                Customer.objects.create(
                    user=user,
                )

                messages.success(request, 'Account was created for ' + username)

                return redirect('signin')

        context = {'form': form}
        return render(request, "termsgen/sign in and signup pages/Get-Started.html", context)

@unauthenticated_user
def signin(request):

            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('dashboard')

                else:
                    messages.info(request, 'Username OR password is incorrect')

            context = {}
            return render(request, "termsgen/sign in and signup pages/Sign-In.html", context)

def logoutUser(request):
    logout(request)
    return redirect('signin')

def forgot(request):
    context = {}
    return render(request, "termsgen/sign in and signup pages/forgot.html", context)

    # INCREASE
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    
    return render(request, "termsgen/sign in and signup pages/Sign-In.html", context)
    
@login_required(login_url='signin')
@allowed_users(allowed_roles=['admin'])
def products(request):
    return render(request, "termsgen/products and templates/product.html",)

@login_required(login_url='signin')
@admin_only
def dashboard(request):
    products = Product.objects.all()

    return render(request, "termsgen/dashboard/edashboard.html", {'products':products})

@login_required(login_url='signin')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    context = {'order':orders}


    return render(request, "termsgen/dashboard/user.html", context)


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

def terms_and_conditions_2(request):
    return render(request, "termsgen/terms and condition/p2-additional-info.html")

def terms_and_conditions_3(request):
    return render(request, "termsgen/terms and condition/p3-security-info.html")

def terms_and_conditions_4(request):
    return render(request, "termsgen/terms and condition/p4-preview-page.html")

def terms_and_conditions_5(request):
    return render(request, "termsgen/terms and condition/p3-success-info.html")

def terms_and_conditions_6(request):
    return render(request, "termsgen/terms and condition/p4-overlay-page.html")