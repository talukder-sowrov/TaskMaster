from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request):
    return render(request, "search.html")

def jobs_list(request):
    return render(request, "jobs_list.html")