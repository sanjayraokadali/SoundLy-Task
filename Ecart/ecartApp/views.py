from django.shortcuts import render
from ecartApp import forms
from ecartApp.forms import QueryModelForm
from ecartApp.models import GenerateItem
from ecartApp.forms import UserRegistrationModelForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

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

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email,password=password)

        if user:
            login(request,user)
            return HomePage(request)
        else:

            print('Someone tried to login and failed')
            print("email: {} , password: {}".format(email,password))
            return HttpResponse('Invalid login details supplied')

    else:

        return render(request,"ecartApp/UserLoginPage.html")

def UserRegistrationPage(request):

    form = UserRegistrationModelForm()

    if request.method == 'POST':

        form = UserRegistrationModelForm(data = request.POST)

        if form.is_valid():

            user = form.save()
            user.set_password(user.password)
            user.save()
            form.save(commit=True)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            print('error')

    return render(request,"ecartApp/UserRegistrationPage.html",{'form':form})

@login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
