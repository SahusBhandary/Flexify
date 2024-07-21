from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from foodAPI import food, findNutrition
from .forms import CreateNewList
import requests

# Create your views here.

def default(request):
    return render(request, 'main/default.html', {"data": food})

def home (response):
    return render(response, "main/home.html", {"name": "test"})

