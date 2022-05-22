from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def home2(request):
    return render(request, 'service.html', {})