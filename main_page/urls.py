from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('project-details/<int:project_id>/', views.project_details, name='project-details'),
    path('', views.index, name='index'),
]
