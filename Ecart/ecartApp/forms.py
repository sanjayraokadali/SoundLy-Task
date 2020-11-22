from django import forms
from ecartApp.models import QueryModel
from django.contrib.auth.models import User
from ecartApp.models import Cart



class QueryModelForm(forms.ModelForm):

    class Meta:

        model = QueryModel

        fields = '__all__'

class UserForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:

        model = User


        fields = ('username','email','first_name','last_name','password')


class CartForm(forms.ModelForm):

    class Meta:

        model = Cart

        fields = '__all__'
