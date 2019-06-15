from django.shortcuts import render
from django.http import HttpResponse
from .models import Bug

def home(request):
    return HttpResponse('Bug Collecter Homepage')

def about(request):
    return render(request, 'about.html')

def bugs_index(request):
    bugs = Bug.objects.all()
    return render(request, 'bugs/index.html', { 'bugs': bugs})

def bugs_detail(request, bug_id):
    bug = Bug.objects.get(id=bug_id)
    return render(request, 'bugs/detail.html', { 'bug': bug})

