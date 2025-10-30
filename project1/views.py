from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, "website\index.html")

def about(request):
    return HttpResponse("Welcome to Project 1 About Page")

def contact(request):
    return HttpResponse("Welcome to Project 1 Contact Page")

