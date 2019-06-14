from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Bug:
    def __init__(self, name, type_bug, description, age):
        self.name = name
        self.type_bug = type_bug
        self.description = description
        self.age = age

bugs = [
    Bug('peter', 'spider', 'creepy crawly', 4),
    Bug('Ralph', 'catapiller', 'chubby and green', 1+"month"),
    Bug('doug', 'fly', 'will fly on your trash', 0),

]

def home(request):
    return HttpResponse('Bug Collecter Homepage')

def about(request):
    return render(request, 'about.html')

def bugs_index(request):
    return render(request, 'bugs/index.html', {'bugs': bugs })

