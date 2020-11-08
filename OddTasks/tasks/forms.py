from django import forms

class SearchForm(forms.Form):
    location = forms.CharField(label='location', max_length=100)
    task = forms.CharField(label='task', max_length=100)