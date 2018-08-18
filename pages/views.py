from django.http import HttpResponse
from django.shortcuts import render

def index(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def about(*args, **kwargs):
    return HttpResponse("<h1>About Page</h1>")

def contact(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")
