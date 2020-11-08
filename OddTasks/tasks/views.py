from django.shortcuts import render
from django.http import HttpResponse
from tasks.helper import populate
from tasks.models import Person


# Create your views here.
def initialize(request):
    populate()
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    return render(request, "index.html")


def search(request):
    if request.method == 'GET':
        user = request.GET.get('task', '')
        location = request.GET.get('location','')
        if user:
            results = Person.objects.filter(Task__icontains=user, Location__icontains=location)
            print(results)

        return render(request, "search.html")
    else:
        return render(request, "search.html")


def jobs_list(request):
    return render(request, "jobs_list.html")