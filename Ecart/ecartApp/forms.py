from django import forms
from ecartApp.models import QueryModel
from django.contrib.auth.models import User
from ecartApp.models import GenerateItem

class FormName(forms.Form):

    Name = forms.CharField()
    Email = forms.EmailField()
    Query = forms.CharField(widget=forms.Textarea)

class QueryModelForm(forms.ModelForm):

    class Meta:

        model = QueryModel

        fields = '__all__'
