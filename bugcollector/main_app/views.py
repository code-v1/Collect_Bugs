from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Bug Collecter Homepage')

def about(request):
    return render(request, 'about.html')
