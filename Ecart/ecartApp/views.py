from django.shortcuts import render
from ecartApp import forms
from ecartApp.forms import QueryModelForm
from ecartApp.forms import UserForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

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

    return render(request,"ecartApp/UserLoginPage.html")

def UserRegistrationPage(request):

    form = UserForm()

    if request.method == 'POST':

        form = UserForm(data = request.POST)

        if form.is_valid():

            user = form.save()

            user.set_password(user.password)

            user.save(commit=True)
            return HomePage(request)

    return render(request,"ecartApp/UserRegistrationPage.html",{'form':form})
