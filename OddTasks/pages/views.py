from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Place that handles various webpages

def home_view(request,*args,**kwargs):
    #return HttpResponse("<h1>TaskMaster</h1>")#string of html code
    return render(request, "home.html", {}) # how to return an html template

def customer_view(request,*args,**kwargs):
    return render(request, "customer.html", {})#string of html code

def worker_view(request,*args,**kwargs):
    return render(request, "worker.html", {})#string of html code
  