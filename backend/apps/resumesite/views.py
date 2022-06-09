from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def service(request):
    return render(request, 'service.html', {})

def aboutus(request):
    return render(request, 'aboutus.html', {})