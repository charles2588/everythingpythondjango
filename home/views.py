from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    peoples = [
        {"name": "Chuck", "age": 10},
        {"name": "Chuck", "age": 10},
        {"name": "Chuck", "age": 10},
        {"name": "Chuck", "age": 18},
    ]
    vegetables = ["tomato", "potato", "celery"]
    template = loader.get_template("home/index.html")
    return render(request, "home/index.html", context={'peoples':peoples})
    # return HttpResponse("Learn Basics of Python")

def about(request):
    return render(request, "home/about.html")

def success_page(request):
    return HttpResponse("<h1>Successful request</h1>")
