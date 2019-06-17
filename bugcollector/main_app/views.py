from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bug , Toy, Photo
from .forms import FeedingForm

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'bugcollecting'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def bugs_index(request):
    bugs = Bug.objects.filter(user=request.user)
    return render(request, 'bugs/index.html', { 'bugs': bugs})

@login_required
def bugs_detail(request, bug_id):
    bug = Bug.objects.get(id=bug_id)
    toys_bug_dosent_have = Toy.objects.exclude(id__in = bug.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'bugs/detail.html', { 
        'bug': bug, 'feeding_form': feeding_form,
        'toys': toys_bug_dosent_have
        })

@login_required
def assoc_toy(request, bug_id, toy_id):
    Bug.objects.get(id=bug_id).toys.add(toy_id)
    return redirect('detail', bug_id=bug_id)

@login_required
def unassoc_toy(request, bug_id, toy_id):
  Bug.objects.get(id=bug_id).toys.add(toy_id)
  return redirect('detail', bug_id=bug_id)

@login_required
def add_feeding(request, bug_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bug_id = bug_id
        new_feeding.save()
    return redirect('detail', bug_id=bug_id)

@login_required
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
   
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class BugUpdate(LoginRequiredMixin,UpdateView):
    model = Bug
    fields = ['type_bug', 'description', 'age']

class BugDelete(LoginRequiredMixin,DeleteView):
    model = Bug
    success_url = '/bugs/'

class ToyList(LoginRequiredMixin,ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin,DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin,CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin,UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin,DeleteView):
  model = Toy
  success_url = '/toys/'

