from django import forms

class SearchForm(forms.Form):
    location = forms.CharField(label='location')
    task = forms.CharField(label='task')