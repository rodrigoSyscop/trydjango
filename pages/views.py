from django.shortcuts import render

def index(request, *args, **kwargs):
    return render(request, 'pages/index.html')

def about(request, *args, **kwargs):
    return render(request, 'pages/about.html')

def contact(request, *args, **kwargs):
    return render(request, 'pages/contact.html')
