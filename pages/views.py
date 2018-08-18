from django.shortcuts import render

def index(request, *args, **kwargs):
    return render(request, 'pages/index.html')

def about(request, *args, **kwargs):
    context = {
        "name": "Rodrigo",
        "age": 34,
        "job": "a Linux SysAdmin"
    }
    return render(request, 'pages/about.html', context)

def contact(request, *args, **kwargs):
    return render(request, 'pages/contact.html')
