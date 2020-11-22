from django.shortcuts import render
from ecartApp import forms
from ecartApp.forms import QueryModelForm
from ecartApp.forms import UserForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from ecartApp.models import GenerateItem,Cart

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def HomePage(request):

    return render(request,'ecartApp/HomePage.html')

def ItemListPage(request):

    item = GenerateItem.objects.all()

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

    return render(request,"ecartApp/SelectedItemPage.html")

def ThankYouPage(request):

    return render(request,"ecartApp/ThankYouPage.html")

def TotalBillPage(request):

    return render(request,'ecartApp/TotalBillPage.html')

def UserLoginPage(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email = email, password = password)

        if user:

            login(request,user)

            return HttpResponseRedirect(reverse('homepage'))
        else:
            return HttpResponse('Invalid Details')
            print('{} {} not found'.format(email,password))
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

    logout(request)

    return HttpResponseRedirect(reverse('homepage'))
