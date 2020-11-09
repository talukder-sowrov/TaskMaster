from django import forms

#forms are needed to accept input from site visitors and then process and respond to the input
#form class descripes how a form works and appears
#form class fields map to HTML <input> elements
#when dealing with a form we instantiate it into the view
#when this form is rendered, it contains the <label> and <input> fields but NOT the <form> so we have to initialize that in HTML
class SearchForm(forms.Form):
    location = forms.CharField(label='location')
    task = forms.CharField(label='task')

class ClickForm(forms.Form):
    task = forms.CharField(label='task')