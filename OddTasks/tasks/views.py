from django.shortcuts import render
from django.http import HttpResponse
from tasks.helper import populate
from tasks.models import Person
from django.template import RequestContext

from .forms import SearchForm
from .forms import ClickForm
from .forms import NameForm

# Create your views here.
#function that takes a web request and returns a web response
#each function contains whatever logic needed to return that response

def initialize(request):
    populate()
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    print("happense1")
    if request.method == 'GET':
        #create a form instance and populate it with the data from the request
        form = ClickForm(request.GET or None)
        form2 = NameForm(request.GET or None)
        if form.is_valid():
            user = request.GET.get('task','')
            if user:
                task_dict = {
                    "Mow Lawn": "ML",
                    "Groceries": "G",
                    "Clean House": "CH",
                    "Snow Shoveling": "SH",
                    "Paint House": "PH",
                    "Rake Leaves": "RL",
                    "Moving": "M",
                    "Plumbing": "P"
                }
                if user in task_dict:
                    results = Person.objects.filter(Task__icontains=task_dict[user])
                    ordered_results = results.order_by('Price')
                    return render(request, "jobs_list.html", {'results': ordered_results})

        elif form2.is_valid():
            user = request.GET.get('name','')
            results = Person.objects.filter(Name__icontains=user)
            ordered_results = results.order_by('Price')
            return render(request, "display_user.html", {'results': ordered_results})
    else:
        form = ClickForm()
    return render(request, "index.html")

#When a page is requested, Django creates an HttpRequest object that contains metadata about the request
#GET method used to request data from a specificed resource
#POST is used to send data to a server to create/update a resource.
#return render combines a given template with a given context dictionary and returns an HttpResonse object with that rendered txt
def search(request):
    if request.method == 'GET':
        #create a form instance and populate it with the data from the request
        form = SearchForm(request.GET or None)
        form2 = NameForm(request.GET or None)
        if form.is_valid():
            user = request.GET.get('task', '')
            location = request.GET.get('location', '')
            if user:
                task_dict = {
                    "Mow Lawn": "ML",
                    "Groceries": "G",
                    "Clean House": "CH",
                    "Snow Shoveling": "SH",
                    "Paint House": "PH",
                    "Rake Leaves": "RL",
                    "Moving": "M",
                    "Plumbing": "P"
                }
                if user in task_dict:
                    results = Person.objects.filter(Task__icontains=task_dict[user], Location__icontains=location)
                    ordered_results = results.order_by('Price')
                    return render(request, "jobs_list.html", {'results': ordered_results})

        elif form2.is_valid():
            user = request.GET.get('name','')
            results = Person.objects.filter(Name__icontains=user)
            ordered_results = results.order_by('Price')
            return render(request, "display_user.html", {'results': ordered_results})

    else:
        form = SearchForm()
    return render(request, "search.html", {'form': form})