from django import forms
from ecartApp.models import QueryModel
from django.contrib.auth.models import User



class QueryModelForm(forms.ModelForm):

    class Meta:

        model = QueryModel

        fields = '__all__'

class UserForm(forms.ModelForm):

    class Meta:

        model = User
        password = forms.CharField(max_length=30, widget = forms.PasswordInput)
        fields = ('username','email','first_name','last_name','password')
