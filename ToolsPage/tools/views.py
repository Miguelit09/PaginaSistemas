from django.shortcuts import render

# Create your views here.

def library(request):
    return render(request, 'library.html', {})

def item(request):
    return render(request, 'item.html', {})

def seeker(request):
    return render(request, 'seeker.html', {})