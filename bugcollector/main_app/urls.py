from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bugs/', views.bugs_index, name='index'),
    path('bugs/<int:bug_id>/', views.bugs_detail, name='detail'),
    path('bugs/create/', views.BugCreate.as_view(), name='bugs_create'),
    path('bugs/<int:pk>/update/', views.BugUpdate.as_view(), name='bugs_update'),
    path('bugs/<int:pk>/delete/', views.BugDelete.as_view(), name='bugs_delete'),
    path('bugs/<int:bug_id>/add_feeding/' , views.add_feeding, name='add_feeding'),
    path('bugs/<int:bug_id>/add_photo/', views.add_photo, name='add_photo'),
    path('bugs/<int:bug_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]