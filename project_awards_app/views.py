from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Project

# Create your views here.
def home(request):
    all_projects = Project.fetch_all_images()
    return render(request,"Moringa_Project_Awards/index.html",{"all_images":all_projects})
