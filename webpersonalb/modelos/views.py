from django.shortcuts import render
from .models import Project

# Create your views here.
def modelos(resquest):
     project = Project.objects.all()
     return render (resquest, "modelos/modelos.html", {"project" : project})
