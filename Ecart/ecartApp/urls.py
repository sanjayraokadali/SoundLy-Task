from django.conf.urls import url
from ecartApp import views

app_name = "ecartApp"

urlpatterns = [

    # url(r'$%',views.HomePage,name='homepage'),
    url(r'^AboutPage/$',views.AboutPage,name='aboutpage'),
    url(r'^ItemListPage/$',views.ItemListPage,name='itemlistpage'),
    url(r'^ContactPage/$',views.ContactPage,name='contactpage'),
    url(r'^PaymentPage/$',views.PaymentPage,name='paymentpage'),
    url(r'^PaymentPage/TotalBillPage/ThankYouPage/$',views.ThankYouPage,name='thankyoupage'),
    url(r'^ItemListPage/SelectedItemPage/$',views.SelectedItemPage,name='selecteditempage'),
    url(r'^PaymentPage/TotalBillPage/$',views.TotalBillPage,name='totalbillpage'),
    url(r'^UserLoginPage/$',views.UserLoginPage,name='userloginpage'),
    url(r'^UserRegistrationPage/$',views.UserRegistrationPage,name='userregistrationpage'),

    ]
