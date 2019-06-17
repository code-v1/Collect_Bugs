from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3

from .models import Bug , Toy, Photo
from .forms import FeedingForm

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'bugcollecting'


def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def bugs_index(request):
    bugs = Bug.objects.all()
    return render(request, 'bugs/index.html', { 'bugs': bugs})

def bugs_detail(request, bug_id):
    bug = Bug.objects.get(id=bug_id)
    toys_bug_dosent_have = Toy.objects.exclude(id__in = bug.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'bugs/detail.html', { 
        'bug': bug, 'feeding_form': feeding_form,
        'toys': toys_bug_dosent_have
        })

def assoc_toy(request, bug_id, toy_id):
    Bug.objects.get(id=bug_id).toys.add(toy_id)
    return redirect('detail', bug_id=bug_id)


def add_feeding(request, bug_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bug_id = bug_id
        new_feeding.save()
    return redirect('detail', bug_id=bug_id)

def add_photo(request, bug_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      print('success')
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, bug_id=bug_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
      print(f"{S3_BASE_URL}{BUCKET}/{key}")
  return redirect('detail', bug_id=bug_id)

class BugCreate(CreateView):
    model = Bug
    fields = '__all__'
    success_url = '/bugs/'

class BugUpdate(UpdateView):
    model = Bug
    fields = ['type_bug', 'description', 'age']

class BugDelete(DeleteView):
    model = Bug
    success_url = '/bugs/'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

