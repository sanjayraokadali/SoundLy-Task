from django import forms

class FormName(forms.Form):

    Name = forms.CharField()
    Email = forms.EmailField()
    Query = forms.CharField(widget=forms.Textarea)
