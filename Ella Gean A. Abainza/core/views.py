from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("Hello, EVSU!")
def home(request):
    return render(request, "home.html", {"title": "Home"})
def about(request):
    context = {
        "title": "About",
        "name": "Ella Gean A. Abainza",        
        "student_id": "2023-25351"   
    }
    return render(request, "about.html", context)

