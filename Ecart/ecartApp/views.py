from django.shortcuts import render
from ecartApp import forms
from ecartApp.forms import QueryModelForm
from ecartApp.forms import UserForm, CartForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from ecartApp.models import GenerateItem
from ecartApp.models import Cart

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def HomePage(request):

    return render(request,'ecartApp/HomePage.html')

def ItemListPage(request):

    item = GenerateItem.objects.all()


    if request.method == 'POST':

        cart = Cart.objects.all()
        item_name = request.POST.get('product_name')
        item_price = request.POST.get('product_price')
        item_quantity = 1



        if Cart.objects.count() == 0:

            cart = Cart(item_name = item_name, item_price = item_price, item_quantity = item_quantity)

        elif item_name == Cart.objects.get(item_name = item_name):

            cart = Cart(item_name = item_name, item_price = item_price, item_quantity = item_quantity + 1)
            
        else:

            cart = Cart(item_name = item_name, item_price = item_price, item_quantity = item_quantity)


        cart.save()

        print('{} : {}'.format(item_name,item_price))

        return HttpResponseRedirect(reverse('ecartApp:selecteditempage'))


    return render(request,'ecartApp/ItemListPage.html',{'item':item})

def PaymentPage(request):

    return render(request,'ecartApp/PaymentPage.html')

def AboutPage(request):

    return render(request,'ecartApp/AboutPage.html')

def ContactPage(request):

    form = QueryModelForm()

    if request.method == 'POST':

        form = QueryModelForm(request.POST)

        if form.is_valid():

            form.save(commit=True)
            return HomePage(request)
        else:
            print('Error!')

    return render(request,'ecartApp/ContactPage.html',{'form':form})


def ProductGallery(request):

    return render(request,'ecartApp/ProductGallery.html')

def SelectedItemPage(request):

    cart = Cart.objects.all()

    if request.method == 'POST':

        item_name = request.POST.get('product_name')

        Cart.objects.get(item_name = item_name).delete()


        return HttpResponseRedirect(reverse('ecartApp:selecteditempage'))


    return render(request,"ecartApp/SelectedItemPage.html",{'cart':cart})

def ThankYouPage(request):

    return render(request,"ecartApp/ThankYouPage.html")

def TotalBillPage(request):

    return render(request,'ecartApp/TotalBillPage.html')

def UserLoginPage(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            print('True')
            login(request,user)

            return HttpResponseRedirect(reverse('homepage'))
        else:
            print('False')
            return HttpResponse('Invalid Details')
    else:

        return render(request,"ecartApp/UserLoginPage.html",{})


def UserRegistrationPage(request):

    registered = False

    form = UserForm()

    if request.method == 'POST':

        form = UserForm(data = request.POST)

        if form.is_valid():

            user = form.save()

            user.set_password(user.password)

            user.save()
            return HomePage(request)
            registered = True

    return render(request,"ecartApp/UserRegistrationPage.html",{'form':form,'registered':registered})

@login_required
def user_logout(request):

    cart = Cart.objects.all()

    cart.delete()

    logout(request)

    return HttpResponseRedirect(reverse('homepage'))

def MyAccountPage(request):

    return render(request,'ecartApp/MyAccountPage.html')
