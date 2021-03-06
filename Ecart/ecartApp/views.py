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
def BasePage(request):

    return render(request,'ecartApp/BasePage.html')


def HomePage(request):

    return render(request,'ecartApp/HomePage.html')

def ItemListPage(request):

    item = GenerateItem.objects.all()


    if request.method == 'POST':

        cart = Cart.objects.all()
        item_name = request.POST.get('product_name')
        item_price = request.POST.get('product_price')
        item_quantity = 1


        if (Cart.objects.count() == 0):
            print('loop 1')
            cart = Cart(item_name = item_name, item_price = item_price, item_quantity = item_quantity)
            cart.save()

        else:
            if Cart.objects.filter(item_name = item_name).exists():

                cart = Cart.objects.get(item_name = item_name)
                cart.item_quantity += 1
                cart.save()


            else:
                cart = Cart(item_name = item_name, item_price = item_price, item_quantity = item_quantity)
                cart.save()


        return HttpResponseRedirect(reverse('ecartApp:itemlistpage'))


    return render(request,'ecartApp/ItemListPage.html',{'item':item})

@login_required
def PaymentPage(request):



    del_cart = Cart.objects.all()

    cart = del_cart

    del_cart.delete()

    return render(request,'ecartApp/PaymentPage.html',{'cart':cart})

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

    if request.method == 'POST':

        order_email = request.POST.get('order_email')
        order_add1 = request.POST.get('order_add1')
        order_city = request.POST.get('order_city')
        order_zip = request.POST.get('order_zip')
        order_number = request.POST.get('order_number')

        order_list = [order_email,order_number,order_add1,order_city,order_zip]



    return render(request,"ecartApp/ThankYouPage.html",context ={'order_list':order_list})

def TotalBillPage(request):

    cart = Cart.objects.all()
    sum = 0


    for price in cart:

        sum += float(price.item_price) * price.item_quantity


    return render(request,'ecartApp/TotalBillPage.html',{'cart':cart,'total':sum})

def UserLoginPage(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            print('True')
            login(request,user)

            return HttpResponseRedirect(reverse('ecartApp:homepage'))
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

    return HttpResponseRedirect(reverse('ecartApp:homepage'))

def MyAccountPage(request):

    return render(request,'ecartApp/MyAccountPage.html')
