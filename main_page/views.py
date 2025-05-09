from django.shortcuts import render, redirect
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'main_page/index.html', {'projects': projects})    

# Create your views here.

def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'main_page/project-details.html', {'project': project})    
