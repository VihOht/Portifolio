from django.shortcuts import render, redirect
from .models import GetInTouch, Project

def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        GetInTouch.objects.create(name=name, email=email, message=message)
        return redirect('/#contact')

    projects = Project.objects.all()
    return render(request, 'main_page/index.html', {'projects': projects})    

# Create your views here.

def project_details(request):
    return render(request, 'main_page/project-details.html')    
