from django import forms
from ecartApp.models import QueryModel
from django.contrib.auth.models import User
from ecartApp.models import GenerateItem
from ecartApp.models import UserRegistrationModel

class FormName(forms.Form):

    Name = forms.CharField()
    Email = forms.EmailField()
    Query = forms.CharField(widget=forms.Textarea)

class QueryModelForm(forms.ModelForm):

    class Meta:

        model = QueryModel

        fields = '__all__'

class UserRegistrationModelForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:

        model = UserRegistrationModel

        fields = '__all__'
