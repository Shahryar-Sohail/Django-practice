from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Project 1 Home Page")

def about(request):
    return HttpResponse("Welcome to Project 1 About Page")

def contact(request):
    return HttpResponse("Welcome to Project 1 Contact Page")

