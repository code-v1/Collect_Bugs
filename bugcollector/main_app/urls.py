from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bugs/', views.bugs_index, name='index'),
    path('bugs/<int:bug_id>/', views.bugs_detail, name='detail'),
]