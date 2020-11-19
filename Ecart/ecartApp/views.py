from django.shortcuts import render


# Create your views here.
def HomePage(request):

    return render(request,'ecartApp/HomePage.html')

def ItemListPage(request):

    return render(request,'ecartApp/ItemListPage.html')

def UserLoginPage(request):

    return render(request,'ecartApp/UserLoginPage.html')

def PaymentPage(request):

    return render(request,'ecartApp/PaymentPage.html')

def AboutPage(request):

    return render(request,'ecartApp/AboutPage.html')

def ContactPage(request):

    return render(request,'ecartApp/ContactPage.html')

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

    return render(request,"ecartApp/UserRegistrationPage.html")
