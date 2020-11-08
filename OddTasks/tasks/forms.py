from django import forms

class SearchForm(forms.Form):
    location = forms.CharField(label = 'Location', max_length = 100)
    task = forms.CharField(label = 'Task')