from django.shortcuts import render
from django.http import HttpResponse
from tasks.helper import populate

# Create your views here.
def initialize(request):
    populate()
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, "index.html")

def search(request):
    return render(request, "search.html")

def jobs_list(request):
    return render(request, "jobs_list.html")